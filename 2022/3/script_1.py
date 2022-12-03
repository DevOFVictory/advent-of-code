with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0

    for line in lines:
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]

        common = list(set(comp1)&set(comp2))[0]

        s += ord(common) - 96 if common.islower() else ord(common) - 38


    print(s)

    ### One Liner
    print(sum((lambda x:ord(x)-96 if x.islower()else ord(x)-38)(list(set(l[:len(l)//2])&set(l[len(l)//2:]))[0]) for l in lines))


