n = int(input())
 
print(n * "  " + '0') 
for i in range(1, n):
    
    print((n - i) * "  " + '0', end=' ')
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i - 1, -1, -1):
        if  j == n - 1:
            print('0')
        else:
            print(j, end=' ')
    print(''.strip().replace("", ""))
 
print("0", end=' ')
for i in range(1, n):
    print(i, end=' ')
for j in range(i + 1, 0, -1):
    print(j, end=' ')
print("0".strip())
 
for i in range(n - 1, -1, -1):
    print((n - i) * "  " + '0', end=' ')
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i - 1, -1, -1):
        print(j, end=' ')
    print(".".strip().replace(".", ""))
