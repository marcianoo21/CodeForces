def dfs(u, x, c):
    if u < 0 or u >= n:
        return
    if a[u] != '?':
        return
    t = 'B' if c == 'R' else 'R'
    a[u] = t
    dfs(u + 1, x, t)
    dfs(u - 1, x, t)

T = int(input())
for _ in range(T):
    n = int(input())
    a = input().strip()
    a = list(a)
    
    for i in range(n):
        if a[i] != '?':
            dfs(i - 1, i, a[i])
            dfs(i + 1, i, a[i])
    
    if a[0] == '?':
        for i in range(n):
            if i % 2 == 0:
                a[i] = 'B'
            else:
                a[i] = 'R'
    
    print(''.join(a))
