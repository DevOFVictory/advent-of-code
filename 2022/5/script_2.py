with open('input.txt') as f:
    lines = f.read()

    supplies, instructions = lines.split('\n\n')

    stacks = [[] for _ in range(int(supplies.splitlines()[-1].split()[-1]))]

    for row in supplies.splitlines()[:-1]:
        for index, box in enumerate(row[1::4]):
            if box != ' ':
                stacks[index].insert(0, box)

    for instruction in instructions.splitlines():
        amount = int(instruction.split()[1])
        orign = int(instruction.split()[3]) - 1
        target = int(instruction.split()[5]) - 1


        moving_boxes = []
        for _ in range(amount):
            box = stacks[orign][-1]
            moving_boxes.append(box)
            stacks[orign] = stacks[orign][:-1]

        stacks[target] += moving_boxes[::-1]

    print(''.join([stack[-1] for stack in stacks]))