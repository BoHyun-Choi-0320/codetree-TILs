A, B = map(int, input().split())

min_num = A
max_num = B

if A > B:
    min_num = B
    max_num = A
elif B > A:
    min_num = A
    max_num = B

for i in range(min_num, max_num+1,2):
    print(i, end=' ')