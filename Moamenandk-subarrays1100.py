t = int(input())

for _ in range(t):
    dividion = 0
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    for i in range(n-1):
        if a[i] > a[i+1]:
            dividion +=1
    if dividion+1 != k:
        print("No") 
    else:
        print("Yes")