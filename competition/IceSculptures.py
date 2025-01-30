n = int(input())
t = list(map(int, input().split()))
sum1 = 0
sum2 = 0
sum3 = 0
if n < 6:
    sum1 += int(sum(t))
    print(sum1)
else:
    if n % 2 != 0:  # 2 9 4 5 6 1 6 4 7 1 3 6 5 6 8
        sum1 += int(sum(t))
        print(sum1)
    else:
        for i in range(0,len(t),2):
            sum1 += int(t[i])
        for i in range(1,len(t),2):
            sum2 += int(t[i])
        for i in range(0,len(t)):
            sum3 += int(t[i])
        
        result = max(sum1, sum2, sum3)
        print(result)


