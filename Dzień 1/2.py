input_file = open("./sonar-scan.txt","r")

scans = input_file.readlines()

betterscans = [int(x) for x in scans]

clearscans = []
for i in range(len(betterscans)-2):
    number = betterscans[i]+betterscans[i+1]+betterscans[i+2]
    clearscans.append(number)

biggerscans = 0
for i in range(len(clearscans)-1):
    if clearscans[i+1] > clearscans[i]:
        biggerscans+=1

print(biggerscans)

input_file.close()