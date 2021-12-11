import queue

input_file = open("./dumbo.txt","r")

octopuses = input_file.readlines()
octopuses = ["0" + elem.strip() + "0" for elem in octopuses]
octopuses = ["0" * len(octopuses[0])] + octopuses + ["0" * len(octopuses[0])]
octopuses = [[int(x) for x in row] for row in octopuses]

#octopuses[y][x]

def IsValid(y, x, list): 
    return list[y][x] not in [9]

def Glowing(y, x, list, queue): #funkcja dodaje +1 jak squid zaświeci i dodaje do kolejki kolejne ośmiorniczki
    for i in range(-1,2):
        for j in range(-1,2):
            list[y+i][x+j] += 1
            if list[y+i][x+j] == 10 and y+i not in [0,11] and x+j not in [0,11]:
                queue.put((y+i, x+j))

def print_list(l):
    for row in l:
        for n in row:
            print(str(n) + " ", end="")
        print("")

times_glowing = 0
for i in range(100):
    for y in range(1, len(octopuses) - 1):
        for x in range(1, len(octopuses) - 1):
            octopuses[y][x] += 1
    glows = queue.SimpleQueue()
    for y in range(1, len(octopuses) - 1):
        for x in range(1, len(octopuses) - 1):
            if octopuses[y][x] == 10:
                glows.put((y, x))
    while glows.empty() == False:
        y, x = glows.get()
        Glowing(y, x, octopuses, glows)
    for y in range(1, len(octopuses) - 1):
        for x in range(1, len(octopuses) - 1):
            if octopuses[y][x] >= 10:
                octopuses[y][x] = 0
                times_glowing += 1

print(times_glowing)

input_file.close()