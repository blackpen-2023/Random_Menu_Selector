def input_filter(name, b):
    a = input(f'{name} : ')
    for i in range(len(b)):
        if a == b[i]:
            a = i
    return a

space = input_filter('(상관없음/배달/홀)', ['상관없음','배달','홀'])

print(space)