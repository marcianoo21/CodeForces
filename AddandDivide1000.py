
def divisions_number(a, b):
    count = 0
    while a > 0:
        a //= b
        count += 1
    return count

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    b_increm = 0
    
    if b == 1:
        b_increm = 1
        b += b_increm
   
    max_val = divisions_number(a, b) + b_increm
    for i in range(9):
        temp = divisions_number(a, b+i)
        max_val = min(max_val, temp + i)
            
    print(max_val + b_increm)
    