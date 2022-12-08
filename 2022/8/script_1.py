with open('input.txt') as f:
    lines = f.read().splitlines()

    grid = [[int(x) for x in y] for y in lines]

    s = 0

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid)-1):
            
                horizontal = grid[y].copy()
                left = horizontal[:x]
                right = horizontal[x+1:len(grid)]

                vertical = [ grid[i][x] for i in range(len(grid)) ]
                top = vertical[:y]
                bottom = vertical[y+1:len(grid)]

                s += max(left) < grid[y][x] or max(right) < grid[y][x] or max(top) < grid[y][x] or max(bottom) < grid[y][x]

    print(s + (2*len(grid) + 2*(len(grid)-2)))