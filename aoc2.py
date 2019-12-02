import math

def fuel(massToTotal):
    fuelToAdd = math.trunc(massToTotal / 3) - 2
    if fuelToAdd <= 0:
        return 0
    else:
        return fuel(fuelToAdd) + fuelToAdd

masses = open("input1.txt", "r")
total = 0
for mass in masses.readlines():
    total += fuel(int(mass))
print(str(total))
