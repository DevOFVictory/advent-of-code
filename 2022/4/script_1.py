with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0


    for line in lines:
        section1 = [i for i in range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1]) + 1)]
        section2 = [i for i in range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1]) + 1)]

        if set(section1).issubset(set(section2)) or set(section2).issubset(set(section1)):
            s += 1
    print(s)


    ### One Liner
    print(sum([1 for l in lines if set([i for i in range(int(l.split(',')[0].split('-')[0]), int(l.split(',')[0].split('-')[1]) + 1)]).issubset(set([i for i in range(int(l.split(',')[1].split('-')[0]), int(l.split(',')[1].split('-')[1]) + 1)])) or set([i for i in range(int(l.split(',')[1].split('-')[0]), int(l.split(',')[1].split('-')[1]) + 1)]).issubset(set([i for i in range(int(l.split(',')[0].split('-')[0]), int(l.split(',')[0].split('-')[1]) + 1)]))]))