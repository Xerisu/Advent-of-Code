INPUT_PATH = "./cursed-numbers.txt"

input_file = open(INPUT_PATH, "r")
temp = input_file.readlines()
input_file.close()


coded_numbers = [[[set(x) for x in x.split()] for x in line.split(" | ")] for line in temp]

good_order = [None,None,None,None,None,None,None]

codes = []
for line in coded_numbers:
    five = []
    six = []
    for letter in line[0]:
        if len(letter) == 2:
            two_segments = letter
        elif len(letter) == 3:
            three_segments = letter
        elif len(letter) == 4:
            four_segments = letter
        elif len(letter) == 5:
            five.append(letter)
        elif len(letter) == 6:
            six.append(letter)
        else:
            seven_segments = letter

    five_segments = five[0].intersection(five[1], five[2])
    six_segments = six[0].intersection(six[1], six[2])
    good_order[0] = three_segments.difference(two_segments)
    good_order[3] = five_segments.intersection(four_segments)
    good_order[6] = five_segments.difference(good_order[0].union(good_order[3]))
    good_order[5] = six_segments.intersection(two_segments) 
    good_order[2] = two_segments.difference(good_order[5])
    good_order[1] = six_segments.difference(good_order[0].union(good_order[5], good_order[6]))
    good_order[4] = seven_segments.difference(good_order[0].union(good_order[0],good_order[2],good_order[3],good_order[1],good_order[5],good_order[6])) 
    code = ''

    for letter in line[1]:
        if len(letter) == 2:
            code += '1'
        elif len(letter) == 3:
            code += '7'
        elif len(letter) == 4:
            code += '4'
        elif letter == seven_segments.difference(good_order[1], good_order[5]):
            code += '2'
        elif letter == seven_segments.difference(good_order[1], good_order[4]):
            code += '3'
        elif letter == seven_segments.difference(good_order[2], good_order[4]):
            code += '5'
        elif letter == seven_segments.difference(good_order[3]):
            code += '0'
        elif letter == seven_segments.difference(good_order[2]):
            code += '6'
        elif letter == seven_segments.difference(good_order[4]):
            code += '9'
        else:
            code += '8'
    codes.append(int(code))

print(codes)
print(sum(codes))