n = int(input())
b = list(map(int, input().split()))
a = []
rest = []
x = 1
a.append(b[0])
rest.append(b[0])

while x < n:
    if b[x-1] >= 0:
        rest.append(b[x])       
    else:   
        rest.pop()
        rest.append(b[x])

    a.append(sum(rest))
    x += 1

print(*a)
