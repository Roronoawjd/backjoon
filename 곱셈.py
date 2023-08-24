a = int(input())
b = int(input())

# 3 위치
print(a*(b%10))

# 4 위치 
print(a*((b%100)//10))

# 5 위치 
print(a*(b//100))

# 6 위치 
print(a*b)