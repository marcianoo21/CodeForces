t = int(input())

for _ in range(t):
    n = int(input())
    strings = []
    binary = ""
    for _ in range(n):
        s = input()
        strings.append(s)
    string_set = set(strings) # set szybszy do wyszukiwania
    for string in strings:
        for x in range(1,len(string)):
            if (string[:x]  in string_set and string[x:] in string_set):
                binary += "1"
                break
        else:
            binary += "0"
    print(binary)

