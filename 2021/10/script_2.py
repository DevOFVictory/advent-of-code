openings = '([{<'
closings = ')]}>'

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def get_closings(seq):
    close = ''
    for i in seq:
        close += closings[openings.index(i)]
    return close


def get_illigal_bracket(brackets):

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
        return (False, stack[::-1])


with open('input.txt') as f:
    lines = f.read().splitlines()
    sum = 0

    scores = []

    for line in lines:
        is_valid, illigal_bracket = get_illigal_bracket(line)

        if not is_valid and 'str' in str(type(illigal_bracket)):
            sum += points.get(illigal_bracket)
        elif not is_valid and 'list' in str(type(illigal_bracket)):
            close_str = get_closings(illigal_bracket)

            score = 0

            for i in close_str:
                score *= 5
                score += list(points.keys()).index(i)+1
            scores.append(score)

    scores = sorted(scores)
    print(scores[int(len(scores)/2)])
