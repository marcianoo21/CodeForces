def gcd(a,b):
    bigger_val = max(a,b)
    smaller_val = min(a,b)
    
    reszta = bigger_val % smaller_val
    
    while reszta != 0:
        temp = smaller_val % reszta
        smaller_val = reszta
        reszta = temp
        
    return smaller_val
  
def odd_in_array(array):
    flag = False
    for ele in array:
        if ele % 2 != 0:
            flag = True
            break
    return flag


t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    result = []
    if odd_in_array(a):
        print(2)
    else:
        for ele in a:
            for x in range(2,ele*2):
                if gcd(x,ele) == 1:
                    result.append(x)
                    break   
                                         
        print(min(result))
        
