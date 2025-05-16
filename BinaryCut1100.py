def mix(s):
    if len(s) < 3:
        return False
    for i in range(2, len(s)):
        if s[i] != s[i % 2]:
            return False
    return True

n = int(input())
# 0101 pokazuje 2 a powinno byc 3
# 01010 pokazuje 3 a powinno byc 4
for _ in range(n):
    s = list(input())
    pieces = 1 
    # print(s)
    if mix(s) == True:
        print(len(s)-1)
    else:
        for x in range(len(s)-1):
            if s[x] == '1' and s[x+1] == '0':
                # print("BOOM")
                pieces += 1
            # print(s[x], s[x+1])
                
        print(pieces)
