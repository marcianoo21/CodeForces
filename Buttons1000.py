n = int(input())
summon = 0
factor = 1

for i in range(n, 1, -1):
    summon += (i-1)*factor
    factor += 1
summon += n
print(summon)

