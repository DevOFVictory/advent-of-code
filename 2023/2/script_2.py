with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0

    for game in lines:

        possible = True

        game_id = int(game.split(':')[0].split(' ')[1])

        sets = game.split(': ')[1].split('; ')
        red_max, green_max, blue_max = 0,0,0

        for game_set in sets:
            colors = game_set.split(', ')

            for color in colors:
                if 'red' in color:
                    red = int(color.split(' ')[0])

                    if red > red_max:
                        red_max = red

                elif 'green' in color:
                    green = int(color.split(' ')[0])

                    if green > green_max:
                        green_max = green
                else:
                    blue = int(color.split(' ')[0])

                    if blue > blue_max:
                        blue_max = blue

        s += red_max * green_max * blue_max

    print(s)


