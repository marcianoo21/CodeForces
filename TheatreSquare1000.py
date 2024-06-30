import math
n, m, a = map(int, input().split())
x = 0
if a == 1:
    x = (m*n)//a

elif a*a > m*n:
    x = 1
else:
    hor = math.ceil(n/a)
    ver = math.ceil(m/a)
    x = hor * ver

print(x)