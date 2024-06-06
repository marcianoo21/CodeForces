a = int(input())
b = int(input())
c = int(input())

result1 = a + b + c
result2 = a + (b * c)
result3 = (a + b) * c
result4 = a * b * c
result5 = a * (b + c)

max_value = max(result1, result2, result3, result4, result5)

print(max_value)
