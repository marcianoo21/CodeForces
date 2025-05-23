def isParity(lst):
    parity = lst[0] % 2
    return all(x % 2 == parity for x in lst)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if isParity()