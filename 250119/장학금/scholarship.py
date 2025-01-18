middleScore, finalScore = map(int, input().split())

if middleScore >= 90:
    if finalScore >= 95 and finalScore <= 100:
        print('100000')
    elif finalScore >= 90:
        print('50000')
else:
    print('0')