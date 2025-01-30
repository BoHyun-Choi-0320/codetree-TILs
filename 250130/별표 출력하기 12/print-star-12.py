n = int(input())

for i in range(n):
    if i == 0:
        for j in range(n):
            print('*',end=' ')
        print()
    elif i % 2 == 0:
        for j in range(n):
            if j > i:
                if j % 2 == 0:
                    print(' ',end=' ')
                else:
                    print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
    else:
        for j in range(n):
            if j >= i:
                if j % 2 == 0:
                    print(' ',end=' ')
                else:
                    print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
