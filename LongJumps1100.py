# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     max_val = 0
#     for i in range(1,n+1):
#         indx = i
#         sum = 0
#         while indx <= n:
#             sum += a[indx-1]
#             indx += a[indx-1]
            
#         if sum > max_val:
#             max_val = sum
        
#     print(max_val)
            
        
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n  # dp[i] = maksymalna suma zaczynając od indeksu i

    for i in range(n - 1, -1, -1):  # idziemy od końca do początku
        jump = i + a[i]
        if jump < n:
            dp[i] = a[i] + dp[jump]
        else:
            dp[i] = a[i]

    print(max(dp))
