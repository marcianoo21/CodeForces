t = int(input())

ans = []

for _ in range(t):
    s = str(input())
    n = len(s)
    counter = 0
    
    while len(s) >= 2:
        if '01' in s:
            s = s.replace('01', '', 1)
            counter += 1
        elif '10' in s:
            s = s.replace('10', '', 1)
            counter += 1
        else:
            break

    if counter % 2 == 0:
        ans.append('NET')
    else:
        ans.append('DA')

print(*ans)
