# map함수는 여러개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장함수이다.
## map 함수의 기본 문법 : map(function, iterable)
### map(int, input().split())는 input받은 값을 공백을 기준으로 나누어 int 형으로 반환한다.

a,b = map(int, input().split())
print(a/b)