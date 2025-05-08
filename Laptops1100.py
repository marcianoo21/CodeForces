n = int(input())
 
laptops = []
for i in range(n):
    
    a, b = map(int, input().split())
    laptops.append((a, b))
    
laptops.sort() # sort po cenie (a)
    
for i in range(n-1):
    if laptops[i][1] > laptops[i + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
