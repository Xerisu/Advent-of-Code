input_file = open("./vents.txt","r")


vents = [x for x in input_file.readlines()]
vents = [elem.strip().split('->') for elem in vents]

for vent in vents:
    i = 0
    for part in vent:
        newpart = part.split(",")
        newpart[0] = int(newpart[0])
        newpart[1] = int(newpart[1])
        vent[i] = newpart
        i+=1




coords = [x for x in vents for x in x for x in x]


size = max(coords) + 1

board = [[0 for _ in range(size)] for _ in range(size)]

for vent in vents:
    if vent[0][0] == vent[1][0]:
        #print("vent x", vent)
        x = vent[0][0]
        y_max = max(vent[0][1], vent[1][1])
        y_min = min(vent[0][1], vent[1][1])
        for y in range(y_min, y_max+1):
            board[x][y] += 1
    elif vent[0][1] == vent[1][1]:
        #print("vent y", vent)
        y = vent[0][1]
        x_max = max(vent[0][0], vent[1][0])
        x_min = min(vent[0][0], vent[1][0])
        for x in range(x_min, x_max+1):
            board[x][y] += 1
    else:
        if vent[0][0] > vent[1][0]:
            x_modifier = -1
        else: 
            x_modifier = 1
        if vent[0][1] > vent[1][1]:
            y_modifier = -1
        else: 
            y_modifier = 1
        x = vent[0][0]
        y = vent[0][1]
        while x != vent[1][0]:
            board[x][y] += 1
            x += x_modifier
            y += y_modifier
        board[x][y] += 1
               
sum = 0
for column in board:
  for n in column:
    if n > 1:
      sum += 1
print(sum)


'''for row in board:
    print(row)'''

input_file.close()