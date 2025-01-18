### Rozwiązanie gdy można zmieniać kolejność grup

# n = int(input())
# s = list(map(int, input().split()))
# if sum(s) % 4 != 0:
#     result = (sum(s) // 4) + 1
# else:
#     result = (sum(s) // 4)

# print(result)





### Rozwiązanie gdy nie można zmieniać kolejności 

# n = int(input())
# s = list(map(int, input().split()))

# limit = 4

# sum = 0
# i = 0
# cache = 0

# while i < n:
#     cache += s[i]
#     if cache < limit:
#         i += 1
#     elif cache == limit:
#         sum += 1
#         i += 1
#         cache = 0
#     else:
#         cache -= s[i]
#         sum += 1
#         cache = 0
# print(sum)

n = int(input())
s = list(map(int, input().split()))

# Liczba grup o rozmiarze 1, 2, 3 i 4
count1 = s.count(1)
count2 = s.count(2)
count3 = s.count(3)
count4 = s.count(4)

# Każda grupa o rozmiarze 4 potrzebuje osobnej taksówki
result = count4

# Grupy o rozmiarze 3 mogą być połączone z grupami o rozmiarze 1
result += count3
count1 = max(0, count1 - count3)

# Dwie grupy o rozmiarze 2 mogą dzielić jedną taksówkę
result += count2 // 2
if count2 % 2 != 0:
    result += 1
    count1 = max(0, count1 - 2)

# Pozostałe grupy o rozmiarze 1 mogą być połączone w taksówki
result += count1 // 4
if count1 % 4 != 0:
    result += 1

print(result)