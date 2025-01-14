a,b,c = map(int, input().split())
arr = [a,b,c]

sumArr = sum(arr)
avgArr = int(sum(arr)/len(arr))
print(sumArr)
print(avgArr)
print(sumArr - avgArr)