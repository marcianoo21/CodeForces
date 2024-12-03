from collections import Counter

n = int(input())
s = str(input())

ans = []
for i in range(n):
    ans.append(s[i:i+2])

my_dict = Counter(ans)
key = next((key for key, value in my_dict.items() if value == max(my_dict.values())), None)
print(key)


