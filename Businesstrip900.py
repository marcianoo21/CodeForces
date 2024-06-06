k = int(input())
x = 0
z = 0
a = list(map(int, input().split()))
ai = sorted(a)
if sum(a) < k:
    print("-1")

elif k > 0:     
    while x < k:
        x += max(ai)
        ai.pop()
        z += 1
    print(z)   
else:
    print(0)
