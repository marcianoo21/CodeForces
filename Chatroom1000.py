s = str(input())
word = 'hello'
i = 0
j = 0


while i < len(s) and j < len(word):
    if s[i] == word[j]:
        j += 1
    i += 1 

if j == len(word):
    print("YES")
else:
    print("NO")