input_file = open("./crabs.txt","r")


crabs = input_file.readlines()
crabs = crabs[0].split(",")

for i in range(len(crabs)):
    crabs[i] = int(crabs[i])

fuel = []
possible_optimal_line = sum(crabs) // len(crabs)
for i in range(-1, 2, 1):
    fuel_use = 0
    for crab in crabs:
        fuel_use += ((1 + abs(crab - possible_optimal_line+i)) * (abs(crab - possible_optimal_line+i))) // 2
    fuel.append(fuel_use)

print(min(fuel))
input_file.close()