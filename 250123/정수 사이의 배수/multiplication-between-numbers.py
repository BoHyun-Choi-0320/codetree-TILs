a,b = map(int, input().split())

total = 0
cnt = 0
for i in range(a,b+1):
    if  i % 5 == 0 or i % 7 ==0:
        total += i
        cnt += 1

div = total/cnt
print(f"{total} {div:.1f}")