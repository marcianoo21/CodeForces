def multi(set):
    summ = 1
    for x in set:
        summ *= x
    return summ

t = int(input())

for _ in range(t):
    counter = 0
    even = 0
    flag = False
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if multi(a) % k == 0:
        print(0)
    elif k == 4: # 3 4  3 5 3
        for x in a:
            if x % 2 == 0:
                even += 1    
            elif (x + 1) % k  == 0:
                flag = True
        if flag:   
            print(1)
        else:    
            counter = max(0, 2 - even)
            print(counter)
    else:
        temp = k
        for x in a:
            rest = k - (x % k)
            if rest < temp: 
                temp = rest
        counter = temp
        print(counter)

