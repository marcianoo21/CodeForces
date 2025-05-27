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
     
# 5 5 - 1-4 2-3 3-2 4-1 (4)
# 6 12   1-4 1-9 2-3 2-8 3-2 3-7 3-12 4-1 4-6 4-11 5-5 5-10 6-4 6-9  (14)
#           2        2         3           3           2        2