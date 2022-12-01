with open('input.txt') as f:
    lines = f.read()

    print(max([sum(list(map(int, bp.splitlines()))) for bp in lines.split('\n\n')]))