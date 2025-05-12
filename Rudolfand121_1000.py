# 2 4 4 5 1 -> 2 4 3 2 0 -> 1 2 2 2 0 -> 0 0 1 2 0 -> NO -> 16 
# 1 3 5 5 2 -> 16 -> YES
# 0 1 3 3 1 -> 8 -> YES


def mono_list(a):
    for x in a:
        if x != a[0]:
            return False
    return True

# print(mono_list([1,1,1,2]))

t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    y = 0
    x = 0
    
    if len(a) == 3:
        if a[1] % 2 == 0 and a[0] == a[1] // 2 and a[2] == a[1] // 2:
            print("YES")
        else:
            print("NO")
    elif mono_list(a):
        print("NO")
    else:
        for i in range(1, len(a)-1):
            if a[i] % 2 == 0:
                y += 1
            else:
                x += 1
            
        if x == 0 or y == 0:
            print("YES")
        else:
            print("NO")
            
        
        