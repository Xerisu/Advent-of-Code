input_file = open("./crabs.txt","r")

crabs = input_file.readlines()
crabs = crabs[0].split(",")

input_file.close()

for i in range(len(crabs)):
    crabs[i] = int(crabs[i])

fuel = []

for i in range(max(crabs)):
    fuel_use = 0
    for crab in crabs:
        fuel_use += abs(crab - i)
    fuel.append(fuel_use)

print(min(fuel))

