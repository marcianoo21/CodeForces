n, m = map(int,input().split())
a = list(map(int,input().split()))

temps_a = set()
distinct_temps_a = [0] * n

for i in range(n - 1, -1, -1):
    temps_a.add(a[i])
    distinct_temps_a[i] = len(temps_a)  

    
for _ in range(m):
    l = int(input())
    print(distinct_temps_a[l-1])
    