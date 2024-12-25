n = int(input())
summon = 0
factor = 1

for i in range(n, 1, -1):
    summon += (i-1)*factor
    factor += 1
summon += n
print(summon)

# dla n=3 3 razy po 1, 2 razy po 2, dla n=4 4 razy po 1, 3 razy po 2, 2 razy po 2 dla n = 4 ma byc 14