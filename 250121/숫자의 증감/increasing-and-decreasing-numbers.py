c,n = input().split()

n = int(n)

if c == 'A':
    i = 1
    for _ in range(n):
        print(i, end =' ')
        i += 1
elif c == 'D':
    for _ in range(n):
        print(n, end =' ')
        n -= 1