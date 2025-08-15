import sys
input = sys.stdin.readline

def find_w(n, c, s):
    sum_s = sum(s)
    sum_s2 = sum(x*x for x in s)
    # f(w) = sum_s2 + 4*w*sum_s + 4*n*w*w
    def f(w):
        return sum_s2 + 4*w*sum_s + 4*n*w*w

    lo = 1
    hi = 1
    while f(hi) < c:
        hi <<= 1
    # binary search lowest w with f(w) >= c
    while lo < hi:
        mid = (lo + hi) // 2
        if f(mid) < c:
            lo = mid + 1
        else:
            hi = mid
    return lo

t = int(input().strip())
out = []
for _ in range(t):
    n_c = input().split()
    while len(n_c) < 2:
        n_c += input().split()
    n = int(n_c[0]); c = int(n_c[1])
    s = list(map(int, input().split()))
    out.append(str(find_w(n, c, s)))

print("\n".join(out))
