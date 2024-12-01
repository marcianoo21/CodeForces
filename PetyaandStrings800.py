import string

first = input().lower()
second = input().lower()

lowercase_alphabet = string.ascii_lowercase

size = len(first)
for char in range(size):
    indx1 =  lowercase_alphabet.index(first[char])
    indx2 =  lowercase_alphabet.index(second[char])
    if indx1 > indx2:
        print("1")
        break
    elif indx1 < indx2:
        print("-1")
        break


if first == second:
    print("0")
   


