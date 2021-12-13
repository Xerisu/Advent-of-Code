input_file = open("./origami.txt","r")

chaos = input_file.readlines()

input_file.close()

def print_list(l):
    for row in l:
        for n in row:
            print(str(n), end="")
        print("")

#to make this work, remove empty line from input
dots = []
instructions = []
for part in chaos:
    if part.startswith('fold'):
        part = part.strip()
        part = part.split(' ')[2]
        part = [part.split('=')[0], int(part.split('=')[1])]
        instructions.append(part)
    else:
        parts = part.strip().split(',')
        for x in range(2):
            parts[x] = int(parts[x])
        dots.append(parts)

max_x = max([item[0] for item in dots])
max_y = max([item[1] for item in dots])

# origami[y][x]

origami = [[0 for x in range(max_x+1)] for y in range(max_y+1)]



for dot in dots:
    origami[dot[1]][dot[0]] += 1
    


for instruction in instructions:
    if instruction[0] == 'y':
        line = instruction[1]
        for y in range(line + 1, len(origami)):
            new_y = 2*line - y
            for x in range(len(origami[y])):
                origami[new_y][x] += origami[y][x]
        origami = origami[0:line] 
    else:
        line = instruction[1]
        for y in range(len(origami)):
            for x in range(line + 1, len(origami[y])):
                new_x = 2*line - x
                origami[y][new_x] += origami[y][x]
            origami[y] = origami[y][0:line]

origami = [ ["#" if item > 0 else " " for item in row] for row in origami ]

print_list(origami)