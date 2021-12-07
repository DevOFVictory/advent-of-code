from statistics import median

with open('input.txt') as f:
    xPositions = list(map(int, f.readline().split(',')))

    average = int(median(xPositions))

    print(sum([abs(i-average) for i in xPositions]))
