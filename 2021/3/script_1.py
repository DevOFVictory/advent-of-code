bits = []

with open('input.txt') as f:
    lines = f.read().splitlines()

    for i in range(12):
        bitsString = ''
        for line in lines:
            bitsString += line[i]
        bits.append(bitsString)

gammaBits = ''
epsilonBits = ''
for b in bits:
    if b.count('1') > b.count('0'):
        gammaBits += '1'
        epsilonBits += '0'
    else:
        gammaBits += '0'
        epsilonBits += '1'

gamma = int(gammaBits, 2)
epsilon = int(epsilonBits, 2)


print(gamma * epsilon)
