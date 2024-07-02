ans = []
def complete_column(n, case, h):
    for x in case:
        if x % 2 == 0:
            h += 1
        else:
            h -= 1
    if abs(h) == n:
        return "YES"
    else:
        return "NO"

t = int(input())
q = 0

for _ in range(t):
    n = int(input()) 
    a = list(map(int, input().split()))
    ans.append(complete_column(n, a, q))

for ele in ans:
    print(ele)
