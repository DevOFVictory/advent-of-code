with open('input.txt') as f:
    lines = f.read().splitlines()

    possible_ids = 0

    for game in lines:

        possible = True

        game_id = int(game.split(':')[0].split(' ')[1])

        sets = game.split(': ')[1].split('; ')

        for game_set in sets:
            colors = game_set.split(', ')
            red, green, blue = 0, 0, 0

            for color in colors:
                if 'red' in color:
                    red = int(color.split(' ')[0])
                elif 'green' in color:
                    green = int(color.split(' ')[0])
                else:
                    blue = int(color.split(' ')[0])

            if red > 12 or green > 13 or blue > 14:
                possible = False
                break

        if possible:
            possible_ids += game_id

    print(possible_ids)


