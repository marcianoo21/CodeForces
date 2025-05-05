n = int(input())

if n % 2 != 0:
    print(0)
else:
    two_sides = n // 2
    if two_sides % 2 != 0:
        res = int(two_sides / 2 - 0.5)
    else:
        res = int(two_sides / 2 - 1)
    print(res)
    # 18 -> 1,1,8,8 2,2,7,7 3,3,6,6 4,4,5,5    4
    # 22 -> 1,1,10,10 2,2,9,9 3,3,8,8 4,4,7,7 5,5,6,6      5
    # 24 -> 1,1,11,11 2,2,10,10 3,3,9,9 4,4,8,8 5,5,7,7  5
    