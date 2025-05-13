
# def solo_zero(a):
#     return all(x == 0 for x in a)

# def at_least_3(a):
#     count = 0
#     for x in a:
#         if x > 0:
#             count += 1
#             if count >= 3:
#                 return True
#     return False

# def any_neg(a):
#     return any(x < 0 for x in a)

# def deleting(a, k):
#     n = len(a)
#     while k <= n - 3 and at_least_3(a) and not any_neg(a):
#         if a[k] > 0:
#             a[k] -= 1
#             a[k+1] -= 2
#             a[k+2] -= 1
#         else:
#             k += 1

#     if solo_zero(a):
#         print("YES")
#         return True
#     else:
#         print("NO")
#         return False
    
    

# t = int(input())

# for _ in range(t):
#     k = 0
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     deleting(a, k)
   
        
def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n - 2):
        if a[i] < 0:
            print('NO')
            return
        op = a[i]
        a[i] -= op
        a[i + 1] -= 2 * op
        a[i + 2] -= op
    if a[-1] != 0 or a[-2] != 0:
        print('NO')
    else:
        print('YES')
    

for _ in range(int(input())):
    solve()