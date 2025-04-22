t = int(input())
for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    min_rices = n * (a-b)
    max_rices = n * (a+b)
    min_pack = c - d
    max_pack = c + d
    if min_rices > max_pack or max_rices < min_pack:
        print("NO")
    else:
        print("YES")