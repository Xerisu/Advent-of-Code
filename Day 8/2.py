input_file = open("./cursed-numbers.txt","r")

temp = input_file.readlines().strip()

input_file.close()

print(temp)
numbers = []
