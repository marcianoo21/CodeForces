k = int(input())
s = str(input())

stats = {}
flag = True
result = ''

for letter in s:
    if letter in stats:
        stats[letter] += 1
    else:
        stats[letter] = 1

for value in stats.values():
    if value % k != 0:
        flag = False

    
if flag == False:
    print(-1)
else:
    for _ in range(k):
        for key, value in stats.items():
            result += key * (value // k)

    print(result)