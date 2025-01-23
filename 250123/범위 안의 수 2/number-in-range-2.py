total = 0
cnt = 0
for _ in range(10):
    n = int(input())
    if 0 <= n and n <=200:
        total+=n
        cnt += 1

print(f"{total} {total/cnt:.1f}")