# 2 4 4 5 1 -> 2 4 3 2 0 -> 1 2 2 2 0 -> 0 0 1 2 0 -> NO -> 16 
# 1 3 5 5 2 -> 16 -> YES
# 0 1 3 3 1 -> 8 -> YES


def solo_zero(a):
    return all(x == 0 for x in a)

def at_least_3(a):
    count = 0
    for x in a:
        if x > 0:
            count += 1
            if count >= 3:
                return True
    return False

def any_neg(a):
    return any(x < 0 for x in a)

def deleting(a, k):
    n = len(a)
    while k <= n - 3 and at_least_3(a) and not any_neg(a):
        if a[k] > 0:
            a[k] -= 1
            a[k+1] -= 2
            a[k+2] -= 1
        else:
            k += 1

    if solo_zero(a):
        print("YES")
        return True
    else:
        print("NO")
        return False
    

# a = [2, 4, 3, 2, 1, 0]
# a = [2, 4, 4, 5, 1]
# k = 0
# ans = []
    

t = int(input())

for _ in range(t):
    k = 0
    n = int(input())
    a = list(map(int, input().split()))
    
    deleting(a, k)
   
        
        
    # ans.append("NO")
    # print(ans)
    # if len(a) == 3:
    #     if a[1] % 2 == 0 and a[0] == a[1] // 2 and a[2] == a[1] // 2:
    #         print("YES")
    #     else:
    #         print("NO")
    # elif mono_list(a):
    #     print("NO")
    # else:
    #     for i in range(1, len(a)-1):
    #         if a[i] % 2 == 0:
    #             y += 1
    #         else:
    #             x += 1
            
    #     if x == 0 or y == 0:
    #         print("YES")
    #     else:
    #         print("NO")
            
        
        