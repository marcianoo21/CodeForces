n = int(input())

a = list(map(int, input().split()))

quotient = a.count(5) // 9
if a.count(5) >= 9 and a.count(0) >= 1:
    print(int("5"*(9*quotient) + "0" *a.count(0)))
else:
    if a.count(0) < 1:
        print(-1)
    else:
        print(0)
    