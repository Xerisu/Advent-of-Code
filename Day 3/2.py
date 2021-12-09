input_file = open("./diagnostic-report.txt","r")

reports = input_file.readlines()

reports_split = []

for report in reports:
    y = int(report) 
    x = [int(a) for a in str(y)]
    reports_split.append(x)

for report in reports_split:
    while len(report) < 12:
        report.insert(0, int(0))


sum1 = 0
sum0 = 0
oxygen_rating = reports_split
i = 0
while len(oxygen_rating) != 1:
    for report in oxygen_rating:
        if report[i] == 0:
            sum0 += 1
        else:
            sum1 += 1

    filter = []
    for oxygen in oxygen_rating:
        if oxygen[i] == 0 and (sum1 >= sum0):
            filter.append(oxygen)
        elif oxygen[i] == 1 and (sum0 > sum1):
            filter.append(oxygen)
    oxygen_rating = [x for x in oxygen_rating if x not in filter]

    sum1 = 0
    sum0 = 0
    i += 1


co2_rating = reports_split
i = 0
while len(co2_rating) != 1:
    for report in co2_rating:
        if report[i] == 0:
            sum0 += 1
        else:
            sum1 += 1

    filter = []
    for co2 in co2_rating:
        if co2[i] == 1 and sum1 >= sum0:
            filter.append(co2)
        elif co2[i] == 0 and sum0 > sum1:
            filter.append(co2)
    co2_rating = [x for x in co2_rating if x not in filter]

    sum1 = 0
    sum0 = 0
    i += 1

oxygen = int("".join([str(x) for x in oxygen_rating[0]]), 2)
co2 = int("".join([str(x) for x in co2_rating[0]]), 2)

print(oxygen_rating[0], oxygen)
print (co2_rating[0], co2)

print (co2*oxygen)

input_file.close()