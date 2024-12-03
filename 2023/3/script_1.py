import string
import math

print('-'.isdigit())

with open('input.txt') as f:
    lines = f.read().splitlines()

    symbols = [] # => (#, x, y)
    numbers = [] # => (15,x, y)

    buffer = ''

    for y in range(len(lines)):
        for x in range(len(lines[y])):

            if lines[y][x].isdigit():
                buffer += lines[y][x]

            else:
                if buffer != '':
                    numbers.append((buffer, x - len(buffer), y))
                    buffer = ''

                if lines[y][x] != '.':
                    symbols.append((lines[y][x], x, y))
        
        if buffer != '':
            numbers.append((buffer, x, y))
            buffer = ''

    print(','.join([i[0] for i in numbers]))

    s = []

    for number in numbers:
        for symbol in symbols:


            px = symbol[1]
            py = symbol[2]
            nx = number[1]
            ny = number[2]
            l = len(number[0])


            for i in range(l):

                if math.sqrt(((nx+i) - px)**2 + (ny - py)**2) <= 1.5:
                    s.append(number)
                    # print(number[0])
                    break
                

    print(len(s))
    print(sum([int(i[0]) for i in s]))


