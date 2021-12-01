with open('input.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    counter = 0

    for i in range(len(lines) - 3):
        if sum(lines[i + 1 : i + 1 + 3]) > sum(lines[i : i + 3]):
            counter += 1

    print(counter)
