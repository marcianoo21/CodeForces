t = int(input())

for _ in range(t):
    a = int(input())
    
    n = 360/(180-a)
    if round(n) == n:
        print("YES")
    else:
        print("NO")