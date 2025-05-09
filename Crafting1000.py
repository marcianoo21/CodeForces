def only_positive(numbers):
    diff = []
    diff[:] = (x for x in numbers if x >= 0)
    return diff
 
def only_negative(numbers):
    diff = []
    diff[:] = (x for x in numbers if x < 0)
    return diff
 
 
t = int(input())
 
for _ in range(t):
    n = int(input())
 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    diffs = []
 
    for i in range(n):
        diffs.append(a[i]-b[i])
    
    if len(only_negative(diffs)) > 1:
        print("NO")
    elif abs(sum(only_negative(diffs))) > min(only_positive(diffs)): 
        print("NO")
    else:
        print("YES")
        