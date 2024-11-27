def process_test_cases(test_cases):
    results = []
    for n, m, a, operations in test_cases:
        max_values = []
        for op in operations:
            if op[0] == '+':
                l, r = op[1], op[2]
                for i in range(n):
                    if l <= a[i] <= r:
                        a[i] += 1
            elif op[0] == '-':
                l, r = op[1], op[2]
                for i in range(n):
                    if l <= a[i] <= r:
                        a[i] -= 1
            max_values.append(max(a))
        results.append(max_values)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    operations = []
    for _ in range(m):
        op = input().split()
        op[1], op[2] = int(op[1]), int(op[2])
        operations.append(op)
    test_cases.append((n, m, a, operations))

# Process test cases
answers = process_test_cases(test_cases)

# Output results
for result in answers:
    print(" ".join(map(str, result)))


    # time exceeded - zrobic by bralo max value i jesli jest w przedziale to tylką ją zmienialo (+1 lub -1)
