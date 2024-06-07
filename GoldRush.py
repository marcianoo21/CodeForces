def can_make_pile(n, m, memo):
    if n == m:
        return "YES"
    if n < m:
        return "NO"
    if n % 3 != 0:
        return "NO"
    
    if (n, m) in memo:
        return memo[(n, m)]
    
    part1 = n // 3
    part2 = 2 * (n // 3)
    
    if can_make_pile(part1, m, memo) == "YES" or can_make_pile(part2, m, memo) == "YES":
        memo[(n, m)] = "YES"
        return "YES"
    
    memo[(n, m)] = "NO"
    return "NO"

def solve(t, test_cases):
    results = []
    for n, m in test_cases:
        memo = {}
        results.append(can_make_pile(n, m, memo))
    return results

t = int(input().strip())
test_cases = []
for _ in range(t):
    n, m = map(int, input().strip().split())
    test_cases.append((n, m))

results = solve(t, test_cases)
for result in results:
    print(result)
