with open('input.txt') as f:
    numbers = list(map(int, f.readline().strip().split(',')))

    for day in range(80):
        for i in range(len(numbers)):
            counter = numbers[i]
            if counter >= 1:
                numbers[i] = counter - 1
            else:
                numbers[i] = 6
                numbers.append(8)
    print(len(numbers))
