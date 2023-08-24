T = int(input())

for _ in range(T):
    _int, _str = input().split()
    _int = int(_int)

    for c in _str:
        print(c * _int, end='')
    print()