n = int(input())

cnt = 0
for i in range(n,0,-1):
    if n % i == 0:
        cnt += 1
        
if cnt == 2:
    print('P')
else:
    print('C')
