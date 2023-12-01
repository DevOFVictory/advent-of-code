with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0

    for line in lines:
        numbers = ''.join(i for i in line if i.isdigit())
        s+= int(numbers[0] + numbers[-1]) 

    print(s)