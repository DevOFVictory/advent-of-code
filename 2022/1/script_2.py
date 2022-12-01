with open('input.txt') as f:
    lines = f.read()

    print(sum(sorted([sum(list(map(int, bp.splitlines()))) for bp in lines.split('\n\n')], reverse=1)[:3]))