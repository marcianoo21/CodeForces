tableCart = input()
carts = list(map(str, input().split()))
a = 0
for cart in carts:
    for char in cart:
        if char in tableCart:
            a += 1

if a > 0:
    print("YES")
else:
    print("NO")