with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0
    for card in lines:
        card_id = int(card.split(':')[0].split()[1])
        winning_numbers = set(map(int, card.split(': ')[1].split(' | ')[0].split()))
        my_numbers = set(map(int, card.split(': ')[1].split(' | ')[1].split()))

        s += int(2 ** (len(my_numbers & winning_numbers)-1))

        
    print(s)
