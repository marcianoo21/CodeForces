t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a)-a[0] > a[-1] or max(a)-a[-1] > a[0] or (a.index(max(a)) == 0 or a.index(max(a)) == -1) and (len(a) != len(list(set(a)))):
        print("NO")
    else:
        print("YES")