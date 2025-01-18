a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

# 1. 수학점수가 높은 사람 출력
# 2. 만약 수학점수가 같으면, 영어 점수가 높은 사람 출력
if a_math > b_math:
    print('A')
elif a_math < b_math:
    print('B')
elif a_math == b_math:
    if a_eng > b_eng:
        print('A')
    else:
        print('B')