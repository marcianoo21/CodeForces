# t = int(input())

# # max 45
# # sum of digits equal to x and all digits are distinct
# for _ in range(t):
#     x = int(input())
#     if x < 10:
#         print(x)
#     elif x > 45:
#         print(-1)
#     elif x == 45:
#         print(123456789)
#     elif x >= 35 and x <= 45:
#         for a in range(56789, 23456790, 1000):
#             nlis = [int(digit) for digit in str(a)]
#             if len(nlis) != len(set(nlis)):
#                 continue
#             if sum(nlis) == x:
#                 break
#         nlis.sort()                
#         print("".join(map(str, nlis)))
#     elif x >= 25 and x <= 34:
#         for a in range(1789, 56789, 100):
#             nlis = [int(digit) for digit in str(a)]
#             if len(nlis) != len(set(nlis)):
#                 continue
#             if sum(nlis) == x:
#                 break     
#         nlis.sort()           
#         print("".join(map(str, nlis)))
#     else:
#         for a in range(19, 790, 10):
#             nlis = [int(digit) for digit in str(a)]
#             if len(nlis) != len(set(nlis)):
#                 continue
#             if sum(nlis) == x:
#                 break         
#         nlis.sort()     
#         print("".join(map(str, nlis)))
                    
        
        
t = int(input())
for _ in range(t):
    n = int(input())
    s = ""
    for i in range(9, 0, -1):
        if n >= i:
            s += str(i)
            n -= i
    s = s[::-1]  # Reverse the string
    if n != 0:
        s = "-1"
    print(s)
