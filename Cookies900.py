n = int(input())
a  = list(map(int, input().split()))
counter = 0

for x in a:
    v = sum(a) - x
    if v % 2 == 0:
        counter += 1
    else:
        continue
print(counter)