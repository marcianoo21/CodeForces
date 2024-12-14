t = int(input())

times = []

for _ in range(t):
    a, b, c ,d = map(int, input().split())

    if b < a and c < d:
        print("-1")
        continue
    elif a == b:
        print(a)
        continue
    res_time = a - b
    diff = c - d
    while res_time > 0:
        res_time -= diff
        b += c 
    print(b)


# time exceeded