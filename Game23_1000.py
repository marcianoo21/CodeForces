n, m = map(int, input().split())
counter = 0

if m % 3 == 0:
    m = m/3
    counter+=1
else:
    m = m/3
    counter+=1

print(counter)

