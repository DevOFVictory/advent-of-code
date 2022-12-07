with open('input.txt') as f:
    lines = f.read().splitlines()

    # lines = """$ cd /
    # $ ls
    # dir a
    # 14848514 b.txt
    # 8504156 c.dat
    # dir d
    # $ cd a
    # $ ls
    # dir e
    # 29116 f
    # 2557 g
    # 62596 h.lst
    # $ cd e
    # $ ls
    # 584 i
    # $ cd ..
    # $ cd ..
    # $ cd d
    # $ ls
    # 4060174 j
    # 8033020 d.log
    # 5626152 d.ext
    # 7214296 k""".splitlines()


    stack = []
    dirs = {}

    take_name = True
    for line in lines[::-1]:
        if line.split()[0].isnumeric():
            stack.append(int(line.split()[0]))
            take_name = True
        elif line.split()[0] == 'dir':
            stack.append(dirs[line.split()[1]])
            take_name = True
        elif '$ cd' in line and take_name:
            folder_name = line.split()[2]
            if folder_name in dirs:
                print('helloo')
            dirs[folder_name] = sum(stack)
            stack.clear()
            take_name = False

    print(sum([i for i in dirs.values() if i <= 100000]))


### Output:   1005501
### Solution: 1315285