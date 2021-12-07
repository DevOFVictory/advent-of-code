with open('input.txt') as f:
    xPositions = list(map(int, f.readline().split(',')))

    average = int(sum(xPositions)/len(xPositions))

    sum = 0

    for i in range(len(xPositions)):
        n = abs(xPositions[i]-average)

        sum += (n*(n+1))/2

    print(int(sum))
