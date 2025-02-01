n = int(input())

num = 11
for i in range(n):
    for j in range(n):
        print(f'{num+2*j}',end=' ')
    print()
    num +=2