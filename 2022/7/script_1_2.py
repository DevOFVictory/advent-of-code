with open('input.txt') as f:
    lines = f.read().splitlines()

    lines = """$ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k""".splitlines()

    path = '/'
    dirs = {}
    buffer_size = 0

    for i in lines[1:]:
        if '$' in i:
            if i.split()[1] == 'cd':
                if i.split()[2] == '..':
                    path = '/'.join(path[:-1].split('/')[:-1]) + '/'
                else:
                    path +=  i.split()[2] + '/'
        else:
            if i.split()[0].isnumeric():
                dirs[path] += int(i.split()[0])
            else:
                print(path)

        dirs[path] = 0

    print(dirs)
