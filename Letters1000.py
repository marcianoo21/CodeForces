n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(b):
    for j in range(a):
        if i > j:
            continue
        elif i <= j:
            print(a.index(j), ) # numer pokoju jeszcze podac
