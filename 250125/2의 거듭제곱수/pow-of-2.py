n = int(input())

i = 0
while True:
    if n  == 1:
        break
    else:
        n //=2
        i+=1
print(i)