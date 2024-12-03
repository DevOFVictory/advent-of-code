with open('input.txt') as f:
    lines = f.read().splitlines()

    s = 0
    for card in lines:
        card_id = int(card.split(':')[0].split()[1])
        winning_numbers = set(map(int, card.split(': ')[1].split(' | ')[0].split()))
        my_numbers = set(map(int, card.split(': ')[1].split(' | ')[1].split()))

        score = int(len(my_numbers & winning_numbers))



        
    print(s)


    def process_cards(index_from, index_to):
        for i in range(index_from, index_to):
            card = lines[i]
            card_id = int(card.split(':')[0].split()[1])
            winning_numbers = set(map(int, card.split(': ')[1].split(' | ')[0].split()))
            my_numbers = set(map(int, card.split(': ')[1].split(' | ')[1].split()))

            score = int(len(my_numbers & winning_numbers))

            process_cards()
