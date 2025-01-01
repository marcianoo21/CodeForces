n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pivot = 0
result = []
a_pivots = []
room_number = []
display = 0

for i in a:
    pivot += i
    a_pivots.append(pivot)

for num1 in b:
    while display < len(a_pivots) and num1 > a_pivots[display]:
        display += 1
    result.append(display + 1)
    if display == 0:
        room_number.append(num1)
    else:
        room_number.append(num1 - a_pivots[display - 1])

for i in range(len(result)):
    print(result[i], room_number[i])