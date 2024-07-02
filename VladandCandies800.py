
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    new_a = list(map(int, sorted(a)))
    
    if len(a) <= 1 and a[0] != 1:
        print("NO")

    elif len(new_a) > 1:
        first_max = max(new_a)
        new_a.pop()
        sec_max = max(new_a)

        if first_max - sec_max >= 2:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
    