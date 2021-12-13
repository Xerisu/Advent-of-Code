input_file = open("./sonar-scan.txt","r")

scans = input_file.readlines()

input_file.close()

betterscans = [int(x) for x in scans]

biggerscans = 0

for i in range(len(betterscans)-1):
    if betterscans[i+1] > betterscans[i]:
        biggerscans += 1

print(biggerscans)

