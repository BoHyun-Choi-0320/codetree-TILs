list_a= input().split()
list_b = input().split()

if (int(list_a[0])>=19 and list_a[1]=='M') or (int(list_b[0])>=19 and list_b[1]=='M'):
    print(1)
else:
    print(0)