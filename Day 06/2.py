input_file = open("./lantern-fish.txt","r")

useless_fish = input_file.readlines()
useless_fish = useless_fish[0].split(",")

input_file.close()

for i in range(len(useless_fish)):
    useless_fish[i] = int(useless_fish[i])

sortedfish = [0,0,0,0,0,0,0,0,0]
for i in range(len(sortedfish)):
    for fish in useless_fish:
        if i == fish:
            sortedfish[i] += 1

temp_fish = [0,0,0,0,0,0,0,0,0]

for i in range(256):
    f = 0
    for fish in sortedfish:
        temp_fish[f] = fish
        f += 1
    for j in range(9):
        if j == 0:
            sortedfish[8] = temp_fish[0]
        else:
            sortedfish[j-1] = temp_fish[j]
    sortedfish[6] += temp_fish[0]                

print(sum(sortedfish))
