n, x = map(int, input().split())
dividers = []

for i in range(1, n+1):
    if x % i == 0 and x / i <= n:
        dividers.append(i)


print(len(dividers))