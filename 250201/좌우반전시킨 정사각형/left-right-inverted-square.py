n = int(input())

for i in range(1,n+1):
    for j in range(n,0,-1):
        print(f'{i*(j)}',end=' ')
    print()

