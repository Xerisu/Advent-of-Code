input_file = open("./commands.txt","r")

commands = input_file.readlines()

commands_list = [x for x in commands]

commands_split = [elem.split() for elem in commands_list]

forward = 0
down = 0
up = 0

for command in commands_split:
    if command[0] == "forward":
        forward += int(command[1])
    if command[0] == "down":
        down += int(command[1])
    if command[0] == "up":
        up += int(command[1])

print((down-up)*forward)


input_file.close()