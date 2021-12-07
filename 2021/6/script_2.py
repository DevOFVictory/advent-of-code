from collections import Counter, OrderedDict
from itertools import islice, cycle


def shift_dict(dct, shift):
    shift %= len(dct)
    return OrderedDict(
        (k, v)
        for k, v in zip(dct.keys(), islice(cycle(dct.values()), shift, None))
    )


with open('input.txt') as f:
    numbers = list(map(int, f.readline().strip().split(',')))

    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    list_dict = dict(Counter(numbers))

    for fishes in list_dict:
        fish_dict[fishes] = list_dict[fishes]

    #print('Initial state:', fish_dict)

    for day in range(256):

        zeros = fish_dict[0]
        fish_dict = dict(shift_dict(fish_dict, 1))
        fish_dict[6] = fish_dict[6] + zeros

    print(sum(fish_dict.values()))
