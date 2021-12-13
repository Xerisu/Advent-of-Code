input_file = open("./lantern-fish.txt","r")

fish = input_file.readlines()
fish = fish[0].split(",")

input_file.close()

for i in range(len(fish)):
    fish[i] = int(fish[i])

#it's pretty unoptimized btw
for i in range(80):
    for j in range(len(fish)):
        if fish[j] == 0:
            fish.append(8)
            fish[j] = 6
        else:
            fish[j] -= 1


print(len(fish))


