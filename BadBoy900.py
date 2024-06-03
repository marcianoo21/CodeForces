def maximize_distance(t, test_cases):
    for case in test_cases:
        n, m, i, j = case
        x1, y1 = 1, 1
        x2, y2 = n, m
        print(x1, y1, x2, y2)

t = int(input())
test_cases = []
for _ in range(t):
    n, m, i, j = map(int, input().split())
    test_cases.append((n, m, i, j))

maximize_distance(t, test_cases)