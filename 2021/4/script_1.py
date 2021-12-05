called_numbers = []


def has_row_won(row):
    return row[0] in called_numbers and row[1] in called_numbers and row[2] in called_numbers and row[3] in called_numbers and row[4] in called_numbers


def has_field_won(field):
    for row_num in field:
        if has_row_won(list(map(int, row_num))):
            return True
    for collumn_num in list(map(list, zip(*field))):
        if has_row_won(list(map(int, collumn_num))):
            return True
    return False


with open('input.txt') as f:
    numbers = list(map(int, f.readline().split(',')))

    fields = [i.strip() for i in f.read().strip().split('\n\n')]
    fields = [i.split('\n') for i in fields]
    fields = [[list(map(int, j.split())) for j in i] for i in fields]

    winner = -1
    counter = -1

    while winner == -1:
        counter += 1
        for index, field in enumerate(fields):
            if has_field_won(field):
                winner = index
                break
            else:
                called_numbers.append(int(numbers[counter]))

    number = numbers[counter]
    unmarked_sum = 0

    for i in fields[winner]:
        for j in i:
            if j not in called_numbers:
                unmarked_sum += j

    print('Number:', number)
    print('Winner: ', winner)
    print('Umarked sum:', unmarked_sum)
    print('Soulution: ', number*unmarked_sum)
