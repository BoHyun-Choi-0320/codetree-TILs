a,b = map(int, input().split())

total5 = 0

if a >= b:
    small,big = b,a
else:
    small,big =a,b

for i in range(small,big+1):
    if i % 5 == 0:
        total5+=i

print(total5)