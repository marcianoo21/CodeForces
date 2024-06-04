t = int(input())

counter = 0

for _ in range(t):   
    n = int(input())
    if n == 1:
        print(0)
    else:
        while n != 1:
            steps = n//2
            squares = n+(n-1)*2+(n-2)
            n -= 2
            counter += steps*squares
     
        print(counter)
        counter = 0