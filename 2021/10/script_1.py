points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def get_illigal_bracket(brackets):

    openings = '([{<'
    closings = ')]}>'

    stack = []
    for i in brackets:
        if i in openings:
            stack.append(i)
        elif i in closings:
            pos = closings.index(i)
            if ((len(stack) > 0) and
                    (openings[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                # print('Expected', closings[openings.index(stack[len(stack)-1])], 'but found', i, 'instead')
                return (False, i)
    if len(stack) == 0:
        return (True, None)
    else:
        return (False, None)


with open('input.txt') as f:
    lines = f.read().splitlines()
    sum = 0

    for line in lines:
        is_valid, illigal_bracket = get_illigal_bracket(line)

        if not is_valid and illigal_bracket != None:
            sum += points.get(illigal_bracket)

    print(sum)
