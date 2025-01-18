y = int(input())

# 1. 4의 배수 -> 윤년 / 아니면 평년
# 2. 100으로 나누어 떨어지면서 400으로 나누어 떨어지지 않는 해는 평년

if y % 4 == 0 and y % 100 != 0:
    print('true')
else:
    print('false')