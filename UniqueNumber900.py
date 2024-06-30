t = int(input())
for _ in range(t):
    n = int(input())
    s = ""
    for i in range(9, 0, -1):
        if n >= i:
            s += str(i)
            n -= i
    s = s[::-1]  
    if n != 0:
        s = "-1"
    print(s)
