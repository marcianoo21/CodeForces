def isParity(lst):
    parity = lst[0] % 2
    return all(x % 2 == parity for x in lst)

def maxOdd(lst):
    return max([x for x in lst if x % 2 != 0])

def minEven(lst):
    soloEvens = [x for x in lst if x % 2 == 0]
    return sorted(soloEvens)[0]

def maxEven(lst):
    soloEvens = [x for x in lst if x % 2 == 0]
    return sorted(soloEvens)[-1]

t = int(input())


for _ in range(t):
    counter = 0
    n = int(input())
    a = list(map(int, input().split()))
   
    while isParity(a) == False:
        min_even_idx = a.index(minEven(a))
        max_odd_idx = a.index(maxOdd(a))
        max_even_idx = a.index(maxEven(a))
        # print("min even idx", min_even_idx,"max even idx", max_even_idx,"max odd idx", max_odd_idx,"ele of max odd", a[max_odd_idx],"ele of min even", a[min_even_idx],"ele of max even", a[max_even_idx])
        if a[min_even_idx] < a[max_odd_idx]:
            a[min_even_idx] += a[max_odd_idx]
        else:
            # print("WAZNE", "MAX EVEN", a[max_even_idx], "MIN EVEN", a[min_even_idx])
            a[max_odd_idx] += a[max_even_idx]
            
        counter += 1
        # print("LISTA A", a)
    print(counter)
            
        
        
        
  