t = int(input())
for _ in range(t):   
    n = int(input())
    if n == 2:
        print(-1)
    else:
        square = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        indexes = [0] * n*n

        for i in range(0, n*n, 2):
            indexes[i] = num
            num += 1
    
        for i in range(1, n*n, 2):
            indexes[i] = num
            num += 1
    
        for i in range(n):
            for j in range(n):
                square[i][j] = indexes[(j % n)+n*i]
        
        for i in range(n):
            for j in range(n):
                print(square[i][j], end=' ')
            print()