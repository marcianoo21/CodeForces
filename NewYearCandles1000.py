a, b = map(int, input().split())

sum = 0
lefts = 0

if b > a:
    print(a)
else:
    sum += a
    while a>= b:
        lefts = a % b
        a = a // b
        sum += a
        a += lefts

    print(sum)

