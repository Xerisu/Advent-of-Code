input_file = open("./diagnostic-report.txt","r")

reports = input_file.readlines()

bits = 12

reports_split = []

for report in reports:
    y = int(report) 
    x = [int(a) for a in str(y)]
    reports_split.append(x)

for report in reports_split:
    while len(report) < bits:
        report.insert(0, int(0))


sum1 = 0
sum0 = 0
gamma_list = []
epsilon_list = []

for i in range(bits):
    for report in reports_split:
        if report[i] == 0:
            sum0 += 1
        else:
            sum1 += 1
    if sum0 > sum1:
        gamma_list.append(int(0))
        epsilon_list.append(int(1)) 
    else:
        gamma_list.append(int(1)) 
        epsilon_list.append(int(0))
    sum1 = 0
    sum0 = 0

gamma = int("".join([str(x) for x in gamma_list]), 2)
epsilon = int("".join([str(x) for x in epsilon_list]), 2)
print(gamma*epsilon)



input_file.close()