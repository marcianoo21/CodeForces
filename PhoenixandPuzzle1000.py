t = int(input())

for _ in range(t):
    n = int(input())
    if (n / 2)**0.5 == round((n / 2)**0.5) or (n / 4)**0.5 == round((n / 4)**0.5) or n == 2 or n == 4:    
        print("YES")
    else:
        print("NO")
