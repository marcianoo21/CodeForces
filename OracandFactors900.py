for s in [*open(0)][1:]:
    n, k = map(int, s.split())
    d = 2
    while n % d:
        d += 1
    print(n + d + 2 * (k - 1))

cases = []
 
def add_div(n):
    if n % 2 == 0:
        n += 2
    else:
        for x in range(3, n+1, 2):
            if n % x == 0:
                n += x
                break 
    return n
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cases.append(add_div(n, k))
 
for _ in range(k):
    add_div(n)

for case in cases:
    print(case)

