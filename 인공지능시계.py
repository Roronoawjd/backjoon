h, m, s = map(int, input().split())
food_time = int(input())

s += food_time
m += s//60
s = s%60
h += m//60
m = m%60
h = h%24
print(h, m, s)