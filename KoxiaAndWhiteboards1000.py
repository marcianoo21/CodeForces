t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = a + b

    res = sorted(c, reverse=True)[:n]
    print(sum(res))
    
