n = int(input()) 

h1, m1 = map(int, input().split())  
res1, res = 1, 1  
for i in range(1, n):
    h, m = map(int, input().split())
    
    if h1 == h and m1 == m:
        res1 += 1
    else:
        res = max(res, res1)
        res1 = 1
    
    h1, m1 = h, m
    
print(max(res, res1))
