import math
n, k = map(int, input().split())
numb = []
for x in range(1, n+1, 2):
    numb.append(x)

#print(numb)
if k > len(numb):
    print(numb[k - math.ceil(n/2)-1]+1)
else:
    print(numb[k-1])