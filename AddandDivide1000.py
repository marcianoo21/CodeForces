import math

def dividions_number(a, b):
    count = 0
    while a > b:
        a = math.floor(a / b)
        count += 1
    if a == b:
        count += 2
    else:
        count += 1  
    return count

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    b_increm = 0
    
    if b == 1:
        b_increm = 1
        b += b_increm
   
    max_val = dividions_number(a, b) + b_increm
    for i in range(3):
        temp = dividions_number(a, b+i)
        if temp + i < max_val:
            max_val = temp + i

    print(max_val + b_increm)
    