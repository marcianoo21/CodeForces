k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

a = 0

for x in range(d):
    if x % n == 0 or x % m == 0 or x % l == 0 or x % k == 0:
        a += 1
    
print(a)