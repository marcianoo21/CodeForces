import math
t = int(input())

sums = []
for _ in range(t):
    n = int(input())
    total_sum = n * (n + 1) // 2
    power = 1
    while power <= n:
        total_sum -= 2 * power
        power *= 2
    sums.append(total_sum)
for sum in sums:
    print(sum)
