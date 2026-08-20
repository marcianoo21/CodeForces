n = int(input())
a = list(map(int, input().split()))

score = 0
highest = 0
a_rev = a[::-1]
highest = a_rev[0]
score += highest

for i in range(1, len(a_rev)):    
    
    if a_rev[i] < highest:
        score += a_rev[i]
        highest = a_rev[i]
        
    else:
        if highest > 0:
            score += highest-1
            highest -= 1

print(score)