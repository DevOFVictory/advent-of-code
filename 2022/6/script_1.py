with open('input.txt') as f:
    line = f.read()

    for i in range(len(line) - 3):
        if len(set(line[i:i+4])) == 4:
            print(i+4)
            break

    ### One Liner
    print([i+4 for i in range(len(line)-3)if len(set(line[i:i+4]))==4][0])