import math

t = int(input())

result = 0

for _ in range(t): 
    a, b, c ,d = map(int, input().split())  
    
    if b < a and c <= d:
        print(-1)
    elif b >= a:
        print(b)
    else:
        diff = c - d
        snooze = math.ceil((a-b) / diff)  
        if snooze < 0:
            snooze = 0
        result = b + (snooze * c)
        print(result)


