# Name: Adventskalender-5
# Description: Caluculates the highest seat id
# Author: DevOFVictory
# Date: 2020/12/06

# Reading input
print('Reading inputs...')
file = open('input.txt')
lines = file.readlines()
file.close()

allSeatIds = []

# Function to split a list seq into num parts
def splitList(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

# Calculates row and collumn for each boarding card
for i in lines:
    i = i.replace('\n', '')
    possibleRows = [o+1 for o in range(128)]
    possibleCollumns = [p+1 for p in range(8)]

    for j in i[:-3]:
        if len(possibleRows) > 1:
            if j == 'F':
                possibleRows = splitList(possibleRows, 2)[0]
            else:
                possibleRows = splitList(possibleRows, 2)[1]
    for j in i[7:10]:
        if len(possibleCollumns) > 1:
            if j == 'R':
                possibleCollumns = splitList(possibleCollumns, 2)[1]
            else:
                possibleCollumns = splitList(possibleCollumns, 2)[0]

    row = int(possibleRows[0])-1
    collumn = int(possibleCollumns[0])-1
    seatId = row * 8 + collumn

    print('Seat', i,  'is in row', row, 'and in collumn', collumn, 'so the seat id is', seatId)

    allSeatIds.append(seatId)

# Loop through all seats and return missing seat, that's mine
minSeat, maxSeat = min(allSeatIds), max(allSeatIds)
mySeat = [seat for seat in range(minSeat, maxSeat + 1) if seat not in allSeatIds][0]


print('')
print('===========================================')
print('\033[94m\033[1m[DONE] \033[92mYour seat id is:\033[4m',mySeat,'\033[0m')
print('===========================================')
