g = int(input())
age = int(input())

if g == 0:
    if age >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if age >= 19:
        print('WOMAN')
    else:
        print('GIRL')