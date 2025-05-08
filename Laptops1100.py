n = int(input())
 
a1 = 0
a2 = 0
res = ''
for i in range(n):
    
    a, b = map(int, input().split())
    if i == 0:
        a1, b1 = a, b
    if a < a1 and b > b1 or a > a1 and b < b1:
        res = 'Happy Alex'
        break
    else:
        res = 'Poor Alex'
        # a1, b1 = a, b
    
print(res)