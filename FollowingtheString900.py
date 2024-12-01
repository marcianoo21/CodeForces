import string

lowercase_alphabet = string.ascii_lowercase
t = int(input())

result = ""
track = {}
index = 0
for _ in range(t):
    size = int(input)
    indices = list(map(int, input().split()))
    for x in range(indices): # tracking ile razy kazdy znak został dodany keys()
        if indices[x] > index:
            track[lowercase_alphabet[1]] = index+1
        else:
            track[lowercase_alphabet[x]] = index
# cos zle myslisz
