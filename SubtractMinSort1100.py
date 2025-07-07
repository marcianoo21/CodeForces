def isNonDecreasing(list):
    pivot = list[0]
    for ele in list:
        if ele < pivot:
            return False
        pivot = ele
    return True

t = int(input())

for  _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n-1):
        min_int = min(a[i], a[i+1])
        # print("MIN", min_int)
        a[i] -= min_int
        a[i+1] -= min_int
    # print("A after", a)
    if isNonDecreasing(a):
        print("YES")
    else:
        print("NO")
   
    
# 4
# 1 4 2 3 - NO
