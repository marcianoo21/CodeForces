q = int(input())

for _ in range(q):
    a, b, n, S = map(int, input().split()) # a - ile monet o wartosci n, b - ilosc monet o wartosci 1, S - szukana suma
    if a*n+b < S:
        print("NO")
    else:
        temp = S // n
        if n * temp + b >= S:
            print("YES")
        else:
            print("NO")
