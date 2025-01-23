n = int(input())

sum_n = 0
for i in range(n):
    num = int(input())
    sum_n += num

print(f"{sum_n} {sum_n/n:.1f}")