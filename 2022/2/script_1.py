def rps(a, b):
    x = a-b
    return int((1/2)*x**3 - (3/2)*x + 1) * 3 + b+1

with open('input.txt') as f:
    lines = f.read().splitlines()

    game = 'ABCXYZ'

    s = 0

    for line in lines:
        a = game.index(line.split()[0])
        b = game.index(line.split()[1]) % 3

        s += rps(a,b)

    print(s)

    ### One Liner
    print(sum((lambda a,b:int(0.5*(a-b)**3-1.5*(a-b)+1)*3+b+1)(*['ABCXYZ'.index(l[i])%3 for i in [0,2]])for l in lines))