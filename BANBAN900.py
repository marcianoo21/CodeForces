import math
t = int(input())
a = 1
for _ in range(t):
    n = int(input())
    b = 3*n
    x = math.ceil(n/2)
    print(x)
    for _ in range(x):
        print(a, b)
        a += 3
        b -= 3
    a = 1
    b = 3*n    
   

    