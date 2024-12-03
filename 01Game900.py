t = int(input())

ans = []

for _ in range(t):
    s = str(input())
    n = len(s)
    counter = 0
    
    while len(s) >= 2:
        if '01' in s:
            przed = s
            s = s.replace('01', '')
            a = (len(przed) - len(s)) // 2
            counter += a
        elif '10' in s:
            przed = s
            s = s.replace('10', '')
            a = (len(przed) - len(s)) // 2
            counter += a
        else:
            break

    if counter % 2 == 0:
        ans.append('NET')
    else:
        ans.append('DA')

print(*ans)
