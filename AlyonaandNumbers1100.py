n, m = map(int, input().split())

counter = 0
x = 1
y = 4
iterations = 0

while x <= n:
    iterations += 1
    if y <= m:
        counter += 1
        y += 5
    else:
        y -= (iterations - 1)*5 +1
        if y < 1:
            y += 5
        x += 1
        iterations = 0
       
print(counter)
