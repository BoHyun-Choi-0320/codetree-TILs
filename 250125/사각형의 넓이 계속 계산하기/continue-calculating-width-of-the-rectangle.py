while True:
    arr = input().split()
    w = int(arr[0])
    h = int(arr[1])
    char = arr[2]
    print(w*h)
    if char == 'C':
        break