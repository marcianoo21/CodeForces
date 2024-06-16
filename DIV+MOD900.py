def find_max_fa(l, r, a):
    def fa(x, a):
        return (x // a) + (x % a)
    
    candidates = [fa(l, a), fa(r, a)]
    x = (r // a) * a - 1

    if l <= x <= r:
        candidates.append(fa(x, a))
    return max(candidates)

t = int(input().strip())
results = []

for _ in range(t):
    l, r, a = map(int, input().strip().split())
    results.append(find_max_fa(l, r, a))

for result in results:
    print(result)
