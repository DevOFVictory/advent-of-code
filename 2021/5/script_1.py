
def get_coords_between(xStart, yStart, xEnd, yEnd):
    points = []

    if xStart == xEnd:
        for i in range(min(yStart, yEnd), max(yStart, yEnd)+1):
            points.append((xStart, i))
    elif yStart == yEnd:
        for i in range(min(xStart, xEnd), max(xStart, xEnd)+1):
            points.append((i, yStart))

    return points


with open('input.txt') as f:
    lines = f.read().splitlines()

    coords = []
    for line in lines:
        start = line.split(' -> ')[0]
        end = line.split(' -> ')[1]

        xStart = int(start.split(',')[0])
        yStart = int(start.split(',')[1])

        xEnd = int(end.split(',')[0])
        yEnd = int(end.split(',')[1])

        for coord in get_coords_between(xStart, yStart, xEnd, yEnd):
            coords.append(coord)

    MyList = ["a", "b", "a", "c", "c", "a", "c"]

    dict_of_counts = {item: coords.count(item) for item in coords}

    filtered = dict((k, v) for k, v in dict_of_counts.items() if v >= 2)

    print(len(filtered))

    # TODO: Optimize Runtime
