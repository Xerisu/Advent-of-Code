input_file = open("./sonar-scan.txt","r")

scans = input_file.readlines()

betterscans = [int(x) for x in scans]



biggerscans = 0

for i in range(len(betterscans)-1):
    if betterscans[i+1] > betterscans[i]:
        biggerscans += 1

print(biggerscans)

input_file.close()