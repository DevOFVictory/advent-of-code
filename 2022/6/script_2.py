with open('input.txt') as f:
    line = f.read()

    for i in range(len(line) - 13):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            break

    ### One Liner
    print([i+14 for i in range(len(line)-13)if len(set(line[i:i+14]))==14][0])