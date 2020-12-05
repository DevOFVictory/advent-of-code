file=open('input.txt')
allLines = file.readlines()
file.close()

rangeList = []
letterList = []
stringList = []

counter = 0

for i in allLines:
    rangeList.append(i.split()[0])
    letterList.append(i.split()[1])
    stringList.append(i.split()[2])

for i in range(len(stringList)):
    rangeMin = int(rangeList[i].split('-')[0])
    rangeMax = int(rangeList[i].split('-')[1])
    letter = letterList[i].replace(':','')
    password = stringList[i]

    x=0

    print(rangeMin,rangeMax,letter,password)

    if password[int(rangeMin)-1]==letter:
        x=x+1
    if password[int(rangeMax)-1]==letter:
        x=x+1
    if x==1:
        counter+=1

print(counter)
