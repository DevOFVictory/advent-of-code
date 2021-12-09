import itertools


def encode(digits, seq):
    sequences = [(0, 1, 2, 4, 5, 6), (2, 5),  (0, 2, 3, 4, 6), (0, 2, 3, 5, 6), (1, 2, 3, 5),
                 (0, 1, 3, 5, 6), (0, 1, 3, 4, 5, 6), (0, 2, 5), (0, 1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 5, 6)]

    idx = sequences[digits]
    return ''.join(sorted(seq[idx] for idx in idx))


def decode(line, seq):
    digits = [encode(i, seq) for i in range(10)]
    ins: list[str] = [''.join(sorted(entry))
                      for entry in line.split(' | ')[0].split()]
    outs: list[str] = [''.join(sorted(entry))
                       for entry in line.split(' | ')[1].split()]

    for i in ins:
        for digit in digits:
            if digit == i:
                break
        else:
            return False, -1
    decoded = ''
    for out in outs:
        decoded += str(digits.index(out))
    return True, int(decoded)


def get_line(line):
    number = -1
    for idx, seq in enumerate(itertools.permutations('abcdefg')):
        judge, number = decode(line, seq)
        if judge:
            break
    return number


with open('input.txt') as f:
    lines = f.read().splitlines()

    print(sum([int(get_line(line)) for line in lines]))
