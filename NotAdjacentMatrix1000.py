def print_2D_list(list):
    for i in range(n):
        for j in range(n):
            print(list[i][j], end=' ')
        print()

t = int(input())

for _ in range(t):   
    n = int(input())
    if n == 2:
        print(-1)
    else:
        square = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        indexes = [0] * n*n

        # separate adjacent numbers in the first half
        for i in range(0, n*n, 2):
            indexes[i] = num
            num += 1

        # separate adjacent numbers in the second half
        for i in range(1, n*n, 2):
            indexes[i] = num
            num += 1

        # convert 1D list on 2D list
        for i in range(n):
            for j in range(n):
                square[i][j] = indexes[(j % n)+n*i]
        
        # induce printing function
        print_2D_list(square)
       