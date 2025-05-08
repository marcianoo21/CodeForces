n = int(input())
 
a1 = 0
b1 = 1
res = ''
for i in range(n):
    
    a, b = map(int, input().split())
    if i == 0 or a1 == b1:
        a1, b1 = a, b
    if a < a1 and b > b1 or a > a1 and b < b1:
        res = 'Happy Alex'
        break
    else:
        res = 'Poor Alex'
    
print(res)




