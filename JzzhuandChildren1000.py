import math
n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
index = ''
s = sorted(a)
if s[-1] < m:
    print(n)
else:
    for x in range(len(a)):
        mod = math.ceil(a[x] / m)
        if mod >= i:
            i = mod
            index = x
    print(index+1)