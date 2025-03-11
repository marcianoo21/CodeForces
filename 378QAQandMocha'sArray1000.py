t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []

    div1 = min(a)
    for ele in a:
        if ele % div1 == 0:
            continue      
        else:
           b.append(ele)
    if len(b) > 0:
        div2 = min(b)
        for x in b:
            if x % div2 == 0:
                continue      
            else:
                c.append(x)
                break
    
    if len(c) > 0:
        print("NO")
    else:
        print("YES")