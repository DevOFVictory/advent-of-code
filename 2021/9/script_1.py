with open('input.txt') as f:
    lines = f.read().splitlines()

    sum = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):

            center = int(lines[y][x])
            top, bottom, left, right = None, None, None, None

            surroundings = []
            try:
                top = int(lines[y-1][x])
                surroundings.append(top)
            except:
                pass

            try:
                bottom = int(lines[y+1][x])
                surroundings.append(bottom)
            except:
                pass

            try:
                right = int(lines[y][x+1])
                surroundings.append(right)
            except:
                pass

            try:
                left = int(lines[y][x-1])
                surroundings.append(left)
            except:
                pass

            is_low = True

            for i in surroundings:
                if i <= center:
                    is_low = False
                    break
            if is_low:
                sum += center + 1

    print(sum)
