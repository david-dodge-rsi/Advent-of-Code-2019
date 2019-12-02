import math

masses = open("input1.txt", "r")
total = 0
for mass in masses.readlines():
    total += math.trunc(int(mass) / 3) - 2
print(str(total))
