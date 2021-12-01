with open('input.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    last = 3000
    counter = 0

    for i in lines:
        if i > last:
            counter += 1
        last = i

    print(counter)
