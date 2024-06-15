n = int(input())
a = list(map(int, input().split()))
a += a
max = 0
valid_ele = 1
counter = 0

for i in range(len(a)):
    if a[i] == valid_ele:
        counter += 1
    else:
        if max < counter:
            max = counter
        counter = 0
print(max)

