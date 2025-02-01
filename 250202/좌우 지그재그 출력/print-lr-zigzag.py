n = int(input())

num = n
for i in range(n):
    if i % 2 == 0:
        for j in range(n-1,-1,-1):
            print(f'{num-j}',end=' ')
    else:
        for j in range(n):
            print(f'{num-j}',end=' ')
    num+=n
    print()
