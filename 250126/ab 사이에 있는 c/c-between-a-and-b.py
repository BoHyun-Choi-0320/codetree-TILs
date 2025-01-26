a,b,c=map(int,input().split())

satisfied = "NO"
for i in range(a,b+1):
    if i % c == 0:
        satisfied = "YES"
        
print(satisfied)