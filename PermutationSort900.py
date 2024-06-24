t = int(input())
liist = []
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    s_permutation = permutation.copy()
    s_permutation.sort()
    if s_permutation == permutation:
        liist.append(0)
    elif permutation[0] == s_permutation[0] or permutation[-1] == s_permutation[-1]: 
        liist.append(1)
    elif permutation[0] == s_permutation[-1] and permutation[-1] == s_permutation[0]:      
        liist.append(3)
    else:
        liist.append(2)

for ele in liist:
    print(ele)