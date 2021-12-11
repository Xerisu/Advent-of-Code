input_file = open("./cave.txt","r")

floor = input_file.readlines()

floor = ["9" + elem.strip() + "9" for elem in floor]
floor = ["9" * len(floor[0])] + floor + ["9" * len(floor[0])]

floor = [[int(x) for x in row] for row in floor]

#floor[y][x]
low_points = []
sum_low_points = 0
for y in range(1, len(floor) - 1):
    for x in range(1, len(floor[0]) - 1):
        if floor[y][x] < floor[y+1][x] and floor[y][x] < floor[y-1][x] and floor[y][x] < floor[y][x+1] and floor[y][x] < floor[y][x-1]:
            sum_low_points += floor[y][x] + 1
            point = (y , x)
            low_points.append(point)



print(sum_low_points)
print(low_points)


