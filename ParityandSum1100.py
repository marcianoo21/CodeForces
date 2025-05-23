def isParity(lst):
    parity = lst[0] % 2
    return all(x % 2 == parity for x in lst)

def maxOdd(lst):
    return max([x for x in lst if x % 2 != 0])

def secondMaxEven(lst):
    soloEvens = [x for x in lst if x % 2 == 0]
    uniqEvens = sorted(list(set(soloEvens)))
    return uniqEvens[-2]

def maxEven(lst):
    soloEvens = [x for x in lst if x % 2 == 0]
    return sorted(soloEvens)[-1]

def evenQuantity(lst):
    return len([x for x in lst if x % 2 == 0])

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if isParity(a):
        print("RES", 0)
    else:
        if secondMaxEven(a) + maxOdd(a) <= maxEven(a):
            print("RES", evenQuantity(a)+1)
        else:
            print("RES",evenQuantity(a))
        
        
       
       
    
# n = [3 ,2, 2, 8] 
# print(secondMaxEven(n))