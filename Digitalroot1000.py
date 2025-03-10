# Digital root of k is d
#  and k Ξ d mod 9 
# ex: k=23 d=5 23 mod 9 = 5 = d

t = int(input())

for _ in range(t):
    k, x = map(int, input().split())

    result = 9*(k-1)+x
    print(result)
    