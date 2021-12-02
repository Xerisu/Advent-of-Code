input_file = open("./commands.txt","r")

commands = input_file.readlines()

commands_list = [x for x in commands]

commands_split = [elem.split() for elem in commands_list]

aim = 0
forward = 0
depth = 0

for command in commands_split:
    if command[0] == "forward":
        forward += int(command[1])
        depth += int(command[1])*aim
    if command[0] == "down":
        aim += int(command[1])
    if command[0] == "up":
        aim -= int(command[1])

print(forward*depth)

input_file.close()