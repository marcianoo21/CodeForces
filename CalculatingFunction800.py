def calculate_f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return -((n + 1) // 2)

n = int(input())

result = calculate_f(n)

print(result)

###   Time limit exceeded

# n = int(input())

# a = 0

# for x in range(1, n+1):
#     if x % 2 == 0:
#         a += x
#     else:
#         y = x*(-1)
#         a += y

# print(a)