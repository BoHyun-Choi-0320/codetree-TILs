a,b = map(int, input().split())

i = a

while a >= b:
    if a % 2 == 0:
        print(a, end = ' ')
    a -= 1 