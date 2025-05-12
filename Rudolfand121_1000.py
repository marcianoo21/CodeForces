# 2 4 4 5 1 -> 2 4 3 2 0 -> 1 2 2 2 0 -> 0 0 1 2 0 -> NO -> 16 
# 1 3 5 5 2 -> 16 -> YES
# 0 1 3 3 1 -> 8 -> YES


def solo_zero(a):
    for x in a:
        if x != 0:
            return False
    return True

def at_least_3(a):
    i = 0
    for x in a:
        if x > 0:
            i += 1
    if i >= 3:
        return True 
    else:
        return False
def deleting(a, k):
    while at_least_3(a) and any_neg(a) != True:
        if a[k] > 0:
            a[k] -= 1
            a[k+1] -= 2
            a[k+2] -= 1
        elif solo_zero(a):
            break
        else:
            k += 1 
        print(a)
        print(a[k], 'iter', k)      
             
def any_neg(a):
    for x in a:
        if x < 0:
            return True
    return False

a = [0, 0, 1, 2, 1, 0]
k = 0
for _ in range(3):
    
    print(deleting(a, k))
# t = int(input())

# for _ in range(t):
#     ans = []
#     k = 0
#     n = int(input())
#     a = list(map(int, input().split()))
#     i = 0
#     while any_neg(a) != True and at_least_3(a) or solo_zero(a) != True:
#         deleting(a, k)
#         print(*a, "iteracja", i)
#         if solo_zero(a):
#             print("YES")
#             break
#         else:
#             print("NO")
#         i += 1
      
#     if solo_zero(a):
#         print("YES")
#     else:
#         print("NO")
        
        
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
            
        
        