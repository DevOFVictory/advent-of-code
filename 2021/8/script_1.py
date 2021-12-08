with open('input.txt') as f:
    lines = f.read().splitlines()
    outputs = [i.split(' | ')[1] for i in lines]

    sum = 0
    for i in outputs:
        digits = i.split()

        for activated_secment in digits:
            if len(activated_secment) == 2 or len(activated_secment) == 4 or len(activated_secment) == 3 or len(activated_secment) == 7:
                sum += 1

    print(sum)
