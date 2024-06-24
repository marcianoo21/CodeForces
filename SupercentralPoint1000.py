n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

supercentral_count = 0
print(points)
for x, y in points:
    has_upper = False
    has_lower = False
    has_left = False
    has_right = False

    for x2, y2 in points:
        if x2 == x and y2 > y:
            has_upper = True
        elif x2 == x and y2 < y:
            has_lower = True
        elif x2 < x and y2 == y:
            has_left = True
        elif x2 > x and y2 == y:
            has_right = True

    if has_upper and has_lower and has_left and has_right:
        supercentral_count += 1

print(supercentral_count)
