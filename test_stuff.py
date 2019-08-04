cycle = 0
hour, hour_previous = 0, 0

for i in range (100):
    print("cycle" + str(cycle))
    print("hour" + str(hour))
    cycle = cycle + 1 if cycle < 95 else 0
    hour, hour_previous = int(cycle / 4), hour
