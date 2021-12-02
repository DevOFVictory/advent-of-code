with open('input.txt') as f:
    lines = f.read().splitlines()

    x, y = 0, 0
    aim = 0

    for i in lines:
        splitted = i.split()

        if splitted[0] == 'forward':
            x += int(splitted[1])
            y += aim*int(splitted[1])
        elif splitted[0] == 'up':
            aim -= int(splitted[1])
        elif splitted[0] == 'down':
            aim += int(splitted[1])

    print(x*y)
