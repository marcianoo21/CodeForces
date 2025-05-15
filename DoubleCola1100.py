boys = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

# po kazdej calej kolejce bedzie razy 2 
n = int(input())

i = 0
while n > 5 * (2 ** i):
    n -= 5 * (2 ** i)
    i += 1

index = (n - 1) // (2 ** i)
print(boys[index])


