n = int(input())
coordinates = list(map(int, input().split()))

even_count = 0
odd_count = 0

for coord in coordinates:
    if coord % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    min_coins = odd_count
else:
    min_coins = even_count

print(min_coins)
