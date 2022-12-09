with open('input.txt') as f:
    lines = f.read().splitlines()

    grid = [[int(x) for x in y] for y in lines]

    distances = []

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid)-1):

            horizontal = grid[y].copy()
            left = horizontal[:x]
            right = horizontal[x+1:len(grid)]

            vertical = [ grid[i][x] for i in range(len(grid)) ]
            top = vertical[:y]
            bottom = vertical[y+1:len(grid)]

            amount_top, amount_right, amount_bottom, amount_left = 0,0,0,0

            for i in top[::-1]:
                amount_top += 1
                if i >= grid[y][x]:
                    break
            
            for i in right:
                amount_right += 1
                if i >= grid[y][x]:
                    break

            for i in bottom:
                amount_bottom += 1
                if i >= grid[y][x]:
                    break

            for i in left[::-1]:
                amount_left += 1
                if i >= grid[y][x]:
                    break

            distances.append(amount_top * amount_right * amount_bottom * amount_left)

    print(max(distances))
