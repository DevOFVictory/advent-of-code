called_numbers = []


def has_row_won(row):
    return row[0] in called_numbers and row[1] in called_numbers and row[2] in called_numbers and row[3] in called_numbers and row[4] in called_numbers


def has__field_won(field):
    for i in field:
        if (has_row_won(i)):
            return True
    for i in list(map(list, zip(*field))):
        if (has_row_won(i)):
            return True
    return False


with open('input.txt') as f:
    numbers = list(map(int, f.readline().split(',')))

    fields = [i.strip() for i in f.read().strip().split('\n\n')]

    winner = -1
    counter = 0

    while winner == -1:
        for index, f in enumerate(fields):
            field = [i.strip().split() for i in f.strip().split('\n')]
            if has__field_won(field):
                winner = index

        called_numbers.append(numbers[counter])
        print(called_numbers)
        counter += 1
    print(winner)
