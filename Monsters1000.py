t = int(input())

def no_greater(a, k):
    for x in a:
        if k < x:
            return False
    return True

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(no_greater(a, k))
    ordered_list = []
    if no_greater(a, k):
       enumer = list(enumerate(a))
       sorted_indexed_list = sorted(enumer, key=lambda x: x[1], reverse=True)
       sorted_indexes = [index + 1 for index, value in sorted_indexed_list]
       print(*sorted_indexes)
       continue  


    
    else:
        for x in range(n):
            if a[x] % k == 0:
                ordered_list.append(x+1)
                a[x] = 0

        for x in range(n):
            if a[x] != 0:
                ordered_list.append(x+1)

        print(*ordered_list)



# a =[1,2,3,4]
# a = sorted(a, reverse=True)
# print(a)