n = int(input())

satisfied = 'N'
for i in range(n-1,1,-1):
    if n % i == 0:
        satisfied = 'C'
print(satisfied)