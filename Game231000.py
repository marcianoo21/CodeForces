n, m = map(int, input().split())

moves = 0
result = m // n

if m % n != 0:
    print("-1")
else:
    while result != 1:
        if result % 3 == 0:
            result = result // 3
            moves += 1
            
        elif result % 2 == 0:
            result = result // 2
            moves += 1
        else:
            moves = -1
            break
    print(moves)