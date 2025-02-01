n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(f'{(j+1)}',end='')
        else:
            print(f'{n-j}',end='')
    print()