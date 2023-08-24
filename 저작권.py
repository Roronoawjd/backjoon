# 평균값 구하는 식 => 평균 값 = 멜로디 개수 / 곡의 개수, 올림해서 평균 값 측정

# 곡의 개수와 평균값
Sing_Count, Average_Price = map(int, input().split())

# 적어도 멜로디 개수는  = 평균 X (곡의 개수-1) +1
melody = Sing_Count * (Average_Price-1) +1
print(melody)
