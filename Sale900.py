n, m = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()

earn = 0
for price in prices:
    if price < 0 and m > 0:
        earn += price
        m -= 1

print(abs(earn))