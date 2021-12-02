input_file = open("./commands.txt","r")

commands = input_file.readlines()

commands_list = [x for x in commands]

commands_split = [elem.split() for elem in commands_list]

forward_commands = []
down_commands = []
up_commands = []

for i in range(len(commands_list)):
    if commands_split[i][0] == "forward":
        forward_commands.append(int(commands_split[i][1]))
    if commands_split[i][0] == "down":
        down_commands.append(int(commands_split[i][1]))
    if commands_split[i][0] == "up":
        up_commands.append(int(commands_split[i][1]))

sum_forward = 0
sum_down = 0
sum_up = 0


for n in forward_commands:
  sum_forward += n

for n in down_commands:
  sum_down += n

for n in up_commands:
  sum_up += n


print((sum_down-sum_up)*sum_forward)


input_file.close()