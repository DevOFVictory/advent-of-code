with open('input.txt') as f:
    lines = f.read().splitlines()

    position = 0
    accumulator = 0

    l = []

    while position not in l:
        splitted = lines[position].split()
        l.append(position)

        command = splitted[0]
        sign = splitted[1][0]
        value = int(splitted[1][1:])

        if command == 'acc':
            if sign == '+':
                accumulator += value
            else:
                accumulator -= value
            position += 1
        elif command == 'jmp':
            if sign == '+':
                position += value
            else:
                position -= value
        else:
            position += 1
    print(accumulator)
#
