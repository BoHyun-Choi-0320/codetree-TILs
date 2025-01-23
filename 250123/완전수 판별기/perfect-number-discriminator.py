n = int(input())

sum_n = 0
for i in range(1, n+1):
    if n % i == 0 and n !=i:
        sum_n+=i

if n == sum_n:
    print('P')
else:
    print('N')