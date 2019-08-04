# coding: utf-8

# import libraries, importantly web3

import json
import pause
import web3
import func_BC
import abi_smartcert
from web3 import Web3, IPCProvider, HTTPProvider

# Establish RPC connection with running node.
web3 = Web3(HTTPProvider("http://localhost:8501"))

pw = "reghee"

smgw1 = web3.toChecksumAddress(0xa6EA94534f45DA9B128F02d0eE5CBF088941b0d2)
smgw2 = web3.toChecksumAddress(0x3E798959d1330Ec81a50eb9D056cf6FfB971a02b)
smgw3 = web3.toChecksumAddress(0xE20585bAD9483D34DdB8a52F9d2c624Bbf1bb939)
owner1 = web3.toChecksumAddress(0x5047774069B3cE1FBc688e182cB98F1367f55511)
owner2 = web3.toChecksumAddress(0x9D9F8aCFFd122d061A40c1ceBe2006959c7d4244)
owner3 = web3.toChecksumAddress(0x71d6e19e5CE1dAEBCD4B79D8CD6C4E32248dC31a)

contract_address = web3.toChecksumAddress(0x7c93bc6ed07fbfcb6fcc92cf6b9b2e4f57a044ab) # result of an Ethereum improvement proposal
contract_abi = json.loads(abi_smartcert.returnABIstr())
contract = web3.eth.contract(abi=contract_abi, address=contract_address)

# print("Accounts being mapped @ block #" + str(web3.eth.blockNumber))
#
# func_BC.py_addSMGW(web3, contract, smgw1, owner1, pw)
# func_BC.py_addSMGW(web3, contract, smgw2, owner2, pw)
# func_BC.py_addSMGW(web3, contract, smgw3, owner3, pw)
#
# func_BC.py_waitForNextBlock(web3, "wait for confirmation of account mapping...")
#
# print("Certificates being created @ block #" + str(web3.eth.blockNumber))

# func_BC.py_createCert(web3, contract, smgw1, owner1, pw)
# func_BC.py_createCert(web3, contract, smgw1, owner1, pw)
# func_BC.py_createCert(web3, contract, smgw1, owner1, pw)
# func_BC.py_createCert(web3, contract, smgw1, owner1, pw)
# func_BC.py_createCert(web3, contract, smgw1, owner1, pw)
# func_BC.py_createCert(web3, contract, smgw1, owner1, pw)

# func_BC.py_waitForNextBlock(web3, "wait for confirmation of certificate creation...")
#
# print("Certificates being transferred @ block #" + str(web3.eth.blockNumber))

# func_BC.py_transferCert(web3, contract, owner1, owner2, 2, pw)
# func_BC.py_transferCert(web3, contract, owner1, owner2, 3, pw)
# func_BC.py_transferCert(web3, contract, owner1, owner3, 4, pw)
# func_BC.py_transferCert(web3, contract, owner1, owner3, 5, pw)
#
# func_BC.py_waitForNextBlock(web3, "wait for confirmation of certificate transfer...")
#
# print("State being returned @ block #" + str(web3.eth.blockNumber))
#
# print(func_BC.py_returnValCertByOwner(web3, contract, owner1, pw))
# print(func_BC.py_returnValCertByOwner(web3, contract, owner2, pw))
# print(func_BC.py_returnValCertByOwner(web3, contract, owner3, pw))
#
# print("Certificates being invalidated @ block #" + str(web3.eth.blockNumber))
#
# func_BC.py_invalidateCert(web3, contract, owner1, 0, pw)
# func_BC.py_invalidateCert(web3, contract, owner1, 1, pw)
# func_BC.py_invalidateCert(web3, contract, owner2, 2, pw)
# func_BC.py_invalidateCert(web3, contract, owner2, 3, pw)
# func_BC.py_invalidateCert(web3, contract, owner3, 4, pw)
# func_BC.py_invalidateCert(web3, contract, owner3, 5, pw)
#
# func_BC.py_waitForNextBlock(web3, "wait for confirmation of certificate invalidation...")
#
# print("State being returned @ block #" + str(web3.eth.blockNumber))
#
# print(func_BC.py_returnValCertByOwner(web3, contract, owner1, pw))
# print(func_BC.py_returnValCertByOwner(web3, contract, owner2, pw))
# print(func_BC.py_returnValCertByOwner(web3, contract, owner3, pw))


print(func_BC.py_smart_cert(web3, contract, smgw1, 0, pw))
print(func_BC.py_smart_cert(web3, contract, smgw1, 1, pw))
print(func_BC.py_smart_cert(web3, contract, smgw1, 2, pw))
print(func_BC.py_smart_cert(web3, contract, smgw1, 3, pw))
print(func_BC.py_smart_cert(web3, contract, smgw1, 4, pw))
print(func_BC.py_smart_cert(web3, contract, smgw1, 5, pw))
