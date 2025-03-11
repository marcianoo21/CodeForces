t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []

    divider1 = min(a)
    for element in a :
        if element % divider1 == 0:
            continue
        else:
            b.append(element)

    if len(b) > 0:
        divider2 = min(b)
        for ele in b:
            if ele % divider2 == 0:
                continue
            else:
                c.append(ele)
                break

    if len(c) > 0:
        print("NO")
    else:
        print("YES")