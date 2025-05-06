import math
# t = int(input())

# for _ in range(t):
#     a, b = map(int, input().split())
#     count = 0
#     if a < b:
#         print("RESULT", 1) 
#     else:
#         if b == 1:
#             b += 1
#             count += 1
#         while a > b:
#             a = math.floor(a / b)
#             count += 1
#             print("A", a, "count", count)
#         if a == b:
#             count += 1
            
    
#     print("RESULT",count)


# a = 50000000 
# b = 6
a = 1337
b = 1
count = 0
b_init = b
# while a > b:
#     a = math.floor(a / b)
#     count += 1
#     print("A", a, "count", count)
    
# print(count+2)

def dividions_number(a, b):
    count = 0
    while a > b:
        a = math.floor(a / b)
        count += 1
    print(count, "A", a, "B", b)  
    if a == b:
        count += 2
    else:
        count += 1  
    return count

if b == 1:
    b += 2
    
max_val = dividions_number(a, b)
print(max_val)
# for i in range(3):
#     b += i
#     print("Dla b: ", b)
#     res = dividions_number(a, b)
#     print("+ ile z dodawania do b", (b - b_init))
#     print("res", res + (b - b_init), "max val", max_val)
#     if res + (b - b_init) < max_val:
#         max_val = res + i

# print(max_val + (b - b_init))
    