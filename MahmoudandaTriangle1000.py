n = int(input())

a = list(map(int, input().split()))

if len(a) < 3:
    print("NO")
else:
    a_sort = sorted(a)
    for i in range(2, n):
       if a_sort[i-2] + a_sort[i-1] > a_sort[i]:
           print("YES")
           break
    else:
        print("NO")