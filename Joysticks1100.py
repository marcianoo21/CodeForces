a1, a2 = map(int, input().split())

time = 0
while a1 > 0 and a2 > 0:
    if a1 + a2 <= 2:
        break
    elif a1 <= 2:
        a1 += 1
        a2 -= 2
    elif a2 <= 2:
        a2 += 1
        a1 -= 2
    elif a1 > a2:
        a2 += 1
        a1 -= 2
    else:
        a1 += 1
        a2 -= 2
    time += 1

print(time)
