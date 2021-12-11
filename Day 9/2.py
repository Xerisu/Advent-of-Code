import queue
from math import prod

input_file = open("./cave.txt","r")

floor = input_file.readlines()

floor = ["9" + elem.strip() + "9" for elem in floor]
floor = ["9" * len(floor[0])] + floor + ["9" * len(floor[0])]

floor = [[int(x) for x in row] for row in floor]

#floor[y][x]
low_points = []
for y in range(1, len(floor) - 1):
    for x in range(1, len(floor[0]) - 1):
        if floor[y][x] < floor[y+1][x] and floor[y][x] < floor[y-1][x] and floor[y][x] < floor[y][x+1] and floor[y][x] < floor[y][x-1]:
            point = (y , x)
            low_points.append(point)

def print_list(l):
    for row in l:
        for n in row:
            print(str(n) + " ", end="")
        print("")

def IsValid(y, x, list):
    return list[y][x] not in [9,'.']

def Color(y, x, list):
    basin_size = 0
    cooler_floor = queue.SimpleQueue()
    cooler_floor.put((y, x))
    while not cooler_floor.empty():
        ty, tx = cooler_floor.get()
        if list[ty][tx] == '.':
            continue
        list[ty][tx] = '.'
        basin_size += 1
        if IsValid(ty-1, tx, list):
            cooler_floor.put((ty-1, tx))
        if IsValid(ty+1, tx, list):
            cooler_floor.put((ty+1, tx))
        if IsValid(ty, tx+1, list):
            cooler_floor.put((ty, tx+1))
        if IsValid(ty, tx-1, list):
            cooler_floor.put((ty, tx-1))
    return basin_size

basins = []
for y, x in low_points:
    basins.append( Color(y, x, floor) )

basins.sort(reverse = True)
print(basins)
print(prod(basins[0:3]))