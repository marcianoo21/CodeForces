n = int(input())

modulo = {
    1: 8,
    2: 4,
    3: 2,
    0: 6,
}
factor = n % 4

if n == 0:
    print(1)
else:
    for x in modulo.keys():
        if x == factor:
            print(modulo[x])


