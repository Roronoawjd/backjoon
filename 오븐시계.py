h, m = map(int, input().split())
cooking_time = int(input())

# 분에 요리시간 더하기
m += cooking_time

# 만약 60분이 넘어갈 경우 시로 넘겨준다.
h += (m//60)
m = (m%60)

# 만약 24시가 넘을 경우 0부터 시작하도록 설정한다.
h = h%24

# 결과 출력
print(h, m)