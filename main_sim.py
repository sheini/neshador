# coding: utf-8

# Author: Sebastian Dirk Lumpp
# Date: 08/07/2019
# Chair of Energy Economics and Application Technology
# Technical University of Munich

# import libraries

import json
#import pause
#import web3
import func_BC
import abi_smartcert
import func_fileIO
from web3 import Web3, IPCProvider, HTTPProvider

# define "cycle" and "hour" variable
# as this chain will run in accelerated time, each cycle(block) will represent 15 minutes
cycle = 0
hour, hour_previous = 0, 0

# define certificate size (in kWh)
cert_size = 1

# paths
chain_name = "test_chain_01"
chain_location = "C:/Users/ga84bas/test_chain_01/"
relative_path_to_key = "chain-data/keys/" + chain_name

# load all accounts
file_acc = open(chain_location + chain_name + "/py_script_info/list_smgw.csv", "r")
list_acc = func_fileIO.readStringArrayFromFile(file_acc)
file_acc.close()

# load generation curves
file_gen = open(chain_location + chain_name + "/py_script_info/input_gen.csv", "r")
list_gen = func_fileIO.readFloatArrayFromFile(file_gen)
file_gen.close()
pv_curve, chp_curve = list_gen[0], list_gen[1]

# connect to chain
# Establish RPC connection with running node.

web3 = Web3(HTTPProvider("http://localhost:8501"))
pw = "reghee"

# configure smart contract (already deployed on chain manually)

contract_address = web3.toChecksumAddress(0x5e00292eb39f84d94a452866a8cd9c4d0aa7fc65)
contract_abi = json.loads(abi_smartcert.returnABIstr())
contract = web3.eth.contract(abi=contract_abi, address=contract_address)

for entry in list_acc:
    func_BC.py_addSMGW(web3, contract, web3.toChecksumAddress(entry[0]), web3.toChecksumAddress(entry[4]), pw)

# wait for new block before beginning simulation
func_BC.py_waitForNextBlock(web3, "Wait for new block before beginning simulation...")
smgw_cum_energy = [0]*100

for sim_step in range(100):
    # for each smgw, calculate generation in this time step, increment energy

    temp_counter = 0
    for smgw in list_acc:
        power_inst = pv_curve[hour] if smgw[2] == "pv" else chp_curve[hour]
        # 0.25 is the quarter hour, smgw[3] is the size of the plant
        smgw_cum_energy[temp_counter] += power_inst * 0.25 * float(smgw[3])
        temp_counter += 1

    # if smgw surpasses threshold, generate certificate for owner(TX), decrement energy "account"
    for i, cum_energy in enumerate(smgw_cum_energy):
        while cum_energy >= cert_size:
            smgw_cum_energy[i] -= cert_size
            cum_energy -= cert_size
            print("Generating certificate for owner # " + str(i) + ". " + str(smgw_cum_energy[i]) + " kWh remaining.")
            func_BC.py_createCert(web3, contract, list_acc[i][0], list_acc[i][4], pw)


    # for each owner, read all valid certificates off blockchain
    list_cert_by_owner = []
    for account in list_acc:
        list_cert_by_owner.append(func_BC.py_returnValCertByOwner(web3, contract, account[4], pw))

    # for each owner, at end of day transfer all valid certificates to next participant on the list
    if hour_previous > hour:
        for i, account in enumerate(list_acc):
            for cert_id in list_cert_by_owner[i]:
                if i < len(list_acc)-1:
                    func_BC.py_transferCert(web3, contract, account[4], list_acc[i+1][4], cert_id, pw)
                else:
                    func_BC.py_transferCert(web3, contract, account[4], list_acc[0][4], cert_id, pw)
    # send out transactions transferring all valid certificates to next participant on list

    # for each owner, invalidate all existing, valid certificates
    # if cycle == 1:
    #     for i, sublist in enumerate(list_cert_by_owner):
    #         for cert_id in sublist:
    #             func_BC.py_invalidateCert(web3, contract, list_acc[i][4], cert_id, pw)
    #     pass
        # invalidate all existing certificates in transactions

    func_BC.py_waitForNextBlock(web3, "Wait for new block before beginning simulation step " + str(sim_step+1) + "...")
    print(list_cert_by_owner)
    # prepare for next step
    cycle = cycle + 1 if cycle < 95 else 0  #95 else 0
    hour, hour_previous = int(cycle / 4), hour
    print(cycle)
    print(hour)
    print(hour_previous)
