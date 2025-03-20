import bisect

n = int(input())  
x = sorted(map(int, input().split()))  
q = int(input())  

results = []
for _ in range(q):
    m = int(input())
    results.append(bisect.bisect_right(x, m))  

print(*results)
