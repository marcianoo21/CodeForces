n = input()
a = 1
if len(n) < 7:
    print("NO")
else:
    for x in range(1, len(n)):
        if n[x-1] == n[x]:
            a += 1
        elif n[x-1] != n[x] and a < 7:
            a = 1
    if a >= 7:
        print("YES")
    else:
        print("NO")