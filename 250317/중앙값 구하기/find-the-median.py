A, B, C = map(int, input().split())

if A > B and A > C:
    if B > C:
        list = [C, B, A]
    else:
        list = [B, C, A]
elif B > A  and B > C:
    if A > C:
        list = [C, A, B]
    else:
        list = [A, C, B]
elif C > A and C > B:
    if A > B:
        list = [B, A, C]
    else:
        list = [A, B, C]

print(list[1])