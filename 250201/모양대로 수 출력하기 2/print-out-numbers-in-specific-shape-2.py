n = int(input())

num_sum = 2
for i in range(n):
    for j in range(n):
        print(f'{num_sum}',end=' ')
        num_sum+=2
        if num_sum >= 10:
            num_sum = 2
    print()