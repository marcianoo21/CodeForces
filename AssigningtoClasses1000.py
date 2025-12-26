t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a_sorted = sorted(a)
    res = a_sorted[n] - a_sorted[n-1]
    print(res)