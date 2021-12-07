from statistics import median
input_file = open("./crabs.txt","r")


crabs = input_file.readlines()
crabs = crabs[0].split(",")

for i in range(len(crabs)):
    crabs[i] = int(crabs[i])


fuel_use = 0
optimal_line = int(median(crabs))
for crab in crabs:
    fuel_use += abs(crab - optimal_line)

print(fuel_use)

input_file.close()