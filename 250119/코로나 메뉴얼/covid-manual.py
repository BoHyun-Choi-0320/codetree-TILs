data = [input().split() for _ in range(3)]
count = sum(1 for x, y in data if x == 'Y' and int(y) >=37)

if count >= 2:
    print('E')
else:
    print('N')