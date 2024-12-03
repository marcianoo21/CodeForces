# # oś liczbowa gdy konik jest na parzystej to skacze w lewo
# # o i gdy jest na nieparzystej skacze w prawo o i co kazdą
# # kolejną rundę jego skok wynosi i+1 input to 
# # (miejsce startowe, ilość skoków) output to (miejsce gdzie skończył)
# 10, 10
# -1, +2,+3, -4, -5,+6, +7, -8, -9, +10
# 10,9,11,14,10,5,11,18,10,1,11
# r = -1 or 1
# n = 10
# x0 = 10
# xn = x0 + (n-1) * r
# s = x0

# # jak zaczynamy od parzystej to mamy 1p,2n,2p,2n,2p...
# 9,8
# 0,1, 2,3,4,5, 6,7,8
# 9,10,8,5,9,14,8,1,9,
# # jak zaczynamy od nieparzystej to mamy 1n,2p,2n,2p,2n...
# +1, -2, -3, +4,+5,-6,-7,+8 = 0 # zgadza sie zaczynał z 9 i skonczył na 9 


# ta wersja time exceeded ale podoba mi sie rozkminka
import time
t = int(input())


start_time = time.time()

for _ in range(t):
    sum = 0
    x, n = map(int, input().split())

    if x % 2 == 0:
        counter = 1
    else:
        counter = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            counter += 1

        if counter % 2 == 0:
            sum += i
        else:
            sum -= i

    print(x + sum)

end_time = time.time()

execution_time = end_time - start_time
print(f"Czas wykonania: {execution_time} sekund")

# zrobic dwie oddzielne sumy dla dodatnich i ujemnych, pętla po __..__..__..