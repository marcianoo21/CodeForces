t = int(input())

def only_one_odd(r,g,b,w):
    goal = 1
    count = 0
    nums = []
    nums.append(r)
    nums.append(g)
    nums.append(b)
    nums.append(w)

    for num in nums:
        if num % 2 == 1:
            count += 1
    if goal == count:
        return True
    else:
        return False

def all_even(r,g,b,w):
    sum = r+g+b+w
    if sum % 2 == 0:
        return True
    else:
        return False
    
def all_the_same(r,g,b,w):
    if r == g == b == w:
        return True
    else:
        return False
    
    
for _ in range(t):
    r,g,b,w = map(int, input().split())
    flag = True
    while not all_even(r,g,b,w) or only_one_odd(r,g,b,w) or all_the_same(r,g,b,w) and flag:
        if r > 0 and g > 0 and b > 0:
            r -= 1
            g -= 1
            b -= 1
            w += 3
        else:
            flag=False
                
            
    # print(f"r: {r}, g: {g}, b: {b}, w: {w}")
    if flag:
        print("YES")
    else:
        print("NO")