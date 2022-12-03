with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0
    groups = [lines[i:i+3] for i in range(0, len(lines), 3)]


    for group in groups:
        comp1 = group[0]
        comp2 = group[1]
        comp3 = group[2]

        common = list(set(comp1)&set(comp2)&set(comp3))[0]

        s += ord(common) - 96 if common.islower() else ord(common) - 38


    print(s)

    ### One Liner
    print(sum((lambda x:ord(x)-96 if x.islower()else ord(x)-38)(list(set(g[0])&set(g[1])&set(g[2]))[0])for g in [lines[i:i+3]for i in range(0,len(lines),3)]))


