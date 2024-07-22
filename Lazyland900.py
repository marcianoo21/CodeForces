n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min = b[0]
val = 0
diff = k - len(set(a))
if len(a) == len(set(a)):
    print(0)
