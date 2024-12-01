expression = map(int, input().split("+"))
s = sorted(expression)
r = ""

for ele in s:
    r += str(ele) + "+"

print(r[:-1])