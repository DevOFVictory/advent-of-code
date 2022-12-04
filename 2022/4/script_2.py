with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0


    for line in lines:
        section1 = [i for i in range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1]) + 1)]
        section2 = [i for i in range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1]) + 1)]

        if len(list(set(section1)&set(section2))) > 0:
            s += 1
    print(s)


    ### One Liner
    print(sum([1 for l in lines if len(list(set([i for i in range(int(l.split(',')[0].split('-')[0]), int(l.split(',')[0].split('-')[1]) + 1)])&set([i for i in range(int(l.split(',')[1].split('-')[0]), int(l.split(',')[1].split('-')[1]) + 1)]))) > 0]))