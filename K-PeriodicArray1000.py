n,k = map(int, input().split())
a = list(map(int, input().split()))

pattern_list = []
diff = 0
diffs = []
for i in range(0, len(a), k):
    current_list = a[i:i+k]
    pattern_list.append(current_list)
  

counter = 0
transposed = list(map(list, zip(*pattern_list)))
for list in transposed:
    counter += min(list.count(1), list.count(2))

print(counter)

    