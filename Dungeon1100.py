t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    health_sum = a + b + c
    # print("suma punktów zycia", health_sum)
    if health_sum / 9 <= min(a,b,c) and (health_sum % 9 == 0):
        print("YES")
    else:
        print("NO")
        
# 52953008 41784347 28668647