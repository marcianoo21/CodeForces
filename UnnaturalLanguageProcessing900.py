c = ["b", "c", "d"]
v = ["a", "e"]
 
def solve():
    new_word = ""
    sylabs = []
    n = int(input())
    word = input()
    fixed_word = word
    x = -1
    while abs(x) < n:
        if fixed_word[x] in c:
            new_word =  word[-3:] + "." 
            word = word[:-3]
            x -= 3
            sylabs.append(new_word)
        else:
            new_word = word[-2:] + "." 
            word = word[:-2]
            x -= 2
            sylabs.append(new_word)
            
    print("".join(sylabs[::-1])[:-1])

for _ in range(int(input())):
    solve()
