import math

a, b = map(int, input().split())
n = int(input())
taxis = []
for _ in range(n):
    x, y, v = map(int, input().split())
    distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    time = distance / v
    taxis.append(time)

print(min(taxis))
