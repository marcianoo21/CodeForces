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

# suma po kazdej iteracji dla x=nieparzysta 1, -1, -4, 0,5,-1,-8,0,9,-1,-12,0, 13 - 
# wnioski: cykl 4 elementowy 1- zaczyna sie od 1 i zmienia co 4(1,5,9,13,...), 2- zawsze -1, 3- zaczyna od -4 i co -4(-4,-8,-12,...), 4- zawsze 0 
# suma po kazdej iteracji dla x=parzysta -1, 1, 4,0,-5,1,8,0,-9,1,12,0
# zrobic n % 4 i dla n% 4 == 2 lub n% 4 == 0 jest stała, dla if n % 4 == 1 to do x dodajemy n lub odejmujemy(dla x parzystego), dla n% 4 == 3 dla parzystych n+1 dla nieparzystych -1*(n+1)
# ta wersja time exceeded ale podoba mi sie rozkminka

import time
t = int(input())
ans = []

start_time = time.time()

for _ in range(t):
  
    result = 0
    x, n = map(int, input().split()) # x - pozycja startowa, n - ilosc skokow

    if n % 4 == 0:
        result = x + 0

    if x % 2 != 0:  
        if n % 4 == 1:
            result = x + n
        elif n % 4 == 2:
            result = x - 1
        elif n % 4 == 3:
            result = x -1*(n+1)
    else:
        if n % 4 == 1:
            result = x - n
        elif n % 4 == 2:
            result = x + 1
        elif n % 4 == 3:
            result = x + (n+1)

    ans.append(result)

end_time = time.time()
print(*ans)
execution_time = end_time - start_time
print(f"Czas wykonania: {execution_time} sekund")

# FUCKING YEAHH