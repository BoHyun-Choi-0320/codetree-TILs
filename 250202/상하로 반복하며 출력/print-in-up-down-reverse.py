n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(f'{1+i}',end='')
        else:
            print(f'{n-i}',end='')
    print()