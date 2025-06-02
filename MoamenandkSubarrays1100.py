t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
    pos = {v: i for i, v in enumerate(b)}
    cnt = 1
    for i in range(n - 1):
        if pos[a[i]] + 1 != pos[a[i + 1]]:
            cnt += 1
    print("YES" if cnt <= k else "NO")