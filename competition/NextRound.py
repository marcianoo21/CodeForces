n, k = map(int, input().split())
a = list(map(int, input().split()))

pivot = a[k-1]
counter = 0
for i in a:
    if i >= pivot and i > 0:
        counter += 1 

print(counter)