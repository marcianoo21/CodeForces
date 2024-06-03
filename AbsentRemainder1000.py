t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = min(a)
    k = 0
    for i in range(len(a)):
        if a[i] != mn:
            print(a[i], mn)
            k += 1
        if k >= n // 2:
            break
