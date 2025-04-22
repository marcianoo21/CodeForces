def find_pivots(list1, q):
    pivots = []
    for i in range(len(list1)):
        if list1[i] > q:
            pivots.append(i)
    return pivots

def devide_lists(pivots, list1):
    lists = []
    if len(pivots) == 0:
        lists.append(list1)
    else:
        for i in range(len(pivots)+1):
            if i == 0:
                lists.append(list1[0:pivots[i]])
            elif i == len(pivots):
                lists.append(list1[pivots[len(pivots)-1]+1:])
            else:
                lists.append(list1[pivots[i-1]+1:pivots[i]])

    return lists

def remove_too_short_lists(lists):
    for listt in lists:
        if len(listt) < k:
            lists.remove(listt)  #len(listt) - k + 1
    return lists

def comb_number(listt, k):
    sum = 0
    for i in range(len(listt)-k+1):
        sum += len(listt) - (k+i) + 1
    return sum



t = int(input())
results = []
for _ in range(t):
    sums = []
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))

    if min(a) > q:
        results.append(0)
    elif max(a) < q: 
        sum1 = 0
        for k in range(k, n+1):
            sum1 += n - k + 1
        results.append(sum1)
    else:
        pivots = find_pivots(a, q)
        lists = devide_lists(pivots, a)
        valid_lists = remove_too_short_lists(lists)
        for listt in valid_lists:
            sums.append(comb_number(listt, k))
        results.append(sum(sums))
        
print(*results)


