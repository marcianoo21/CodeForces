l, r = map(int, input().split())

solutions_ammount = (r-l+1) // 2

if (l >= r) or ((r - l) % 2 != 1):
    print("NO")
else:
    print("YES")
    for i in range(solutions_ammount):
       print(l+i*2, " ", l+i*2+1) 