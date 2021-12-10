with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

height_map = {}
for y, row in enumerate(lines):
    for x, height in enumerate(row):
        height_map[(x, y)] = int(height)

low_points = []
sum = 0
for coords, height in height_map.items():
    x, y = coords
    neighbours = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    lowest = True
    for neighbour in neighbours:
        if height_map.get(neighbour, 10) <= height:
            lowest = False
            break

    if lowest:
        low_points.append(coords)
        sum += height + 1

basin_sizes = []
for low_point in low_points:
    part_of_basin = set([low_point])

    coords_to_check_stack = [low_point]
    while coords_to_check_stack:
        x, y = coords_to_check_stack.pop()
        adjacent = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        for neighbour in adjacent:
            neighbour_height = height_map.get(neighbour, 0)
            if neighbour_height > height_map[(x, y)] and neighbour_height != 9:
                part_of_basin.add(neighbour)
                coords_to_check_stack.append(neighbour)

    basin_sizes.append(len(part_of_basin))

basin_sizes.sort(reverse=True)

largest_three_product = 1
for size in basin_sizes[:3]:
    largest_three_product *= size

print(largest_three_product)
