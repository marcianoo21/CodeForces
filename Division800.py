t = int(input())


def num(a):
    if a >= 1900:
        return 1
    elif a >= 1600 and a <= 1899:
        return 2
    elif a >= 1400 and a <=1599:
        return 3
    else:
        return 4
    

for _ in range(t):
    n = int(input())

    result = num(n)
    print(f"Division {result}")