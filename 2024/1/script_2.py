with open('input.txt') as f:
    lines = f.read().splitlines()
    s = 0

    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for line in lines:
        for i, j in digits.items():
            line = line.replace(i, i + j + i)

        numbers = ''.join(i for i in line if i.isdigit())
        s+= int(numbers[0] + numbers[-1]) 

    print(s)