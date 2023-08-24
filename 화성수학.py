# @는 3을 곱한다.
# %는 5를 더한다.
# #은 7을 뺀다.

T = int(input())

for _ in range(T):
    lst = input().split()
    lst[0] = float(lst[0])

    result = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == '@':
            result = result * 3
        elif lst[i] == '%':
            result = result + 5
        else:
            result = result - 7
    
    print("{:.2f}".format(result))

