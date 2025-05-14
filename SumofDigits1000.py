n = input()
iter = 0

if len(n) <= 1:
    print(0)
else: 
    while len(n) != 1:
        ns = list(n)
        intn = [int(x) for x in ns]
        n = sum(intn)
        n = str(n)
        iter += 1
            
    print(iter)
    