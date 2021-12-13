input_file = open("./cursed-numbers.txt","r")

temp = input_file.readlines()
temp = [elem.strip().split('|') for elem in temp]

input_file.close()

numbers = []

for i in temp:
    numbers.append(i[1])

numbers = [x.strip().split(' ') for x in numbers]
numbers = [x for x in numbers for x in x]

one_four_seven_eight = 0

for number in numbers:
    if len(number) in [2, 3, 4, 7]:
        one_four_seven_eight += 1
    
print(one_four_seven_eight)