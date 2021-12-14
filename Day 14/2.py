input_file = open("./polymer.txt","r")

input_list = input_file.readlines()

input_file.close()

polymer = input_list[0].strip()

first_letter = polymer[0]
last_letter = polymer[-1]

input_list = [[x.strip() for x in elem.split('->')] for elem in input_list[2:]]

instructions = {input_list[i][0]: input_list[i][1] for i in range(len(input_list))}
polymer_templates = {input_list[i][0]: 0 for i in range(len(input_list))}
elements = {input_list[i][1]: 0 for i in range(len(input_list))}

for i in range(len(polymer)-1):
    pair = polymer[i] + polymer[i+1]
    polymer_templates[pair] += 1

for key in instructions:
    two_parts = [key[0] + instructions[key], instructions[key] + key[1]]
    instructions[key] = two_parts


for i in range(40):
    changing_polymer_templates = {input_list[i][0]: 0 for i in range(len(input_list))}
    for key in instructions:
        changing_polymer_templates[ instructions[key][0] ] += polymer_templates[key] 
        changing_polymer_templates[ instructions[key][1] ] += polymer_templates[key]    
    polymer_templates = changing_polymer_templates

elements[first_letter] += 1
elements[last_letter] +=1
for key in polymer_templates:
    elements[key[0]] += polymer_templates[key]
    elements[key[1]] += polymer_templates[key]

for key in elements:
    elements[key] = elements[key] // 2

values = list(elements.values())

print(max(values) - min(values))