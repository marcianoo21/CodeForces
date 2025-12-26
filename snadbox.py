# def isNonDecreasing(list):
#     pivot = list[0]
#     for ele in list:
#         if ele < pivot:
#             return False
#         pivot = ele
#     return True

# t = int(input())

# for  _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     for i in range(n-1):
#         min_int = min(a[i], a[i+1])
#         # print("MIN", min_int)
#         a[i] -= min_int
#         a[i+1] -= min_int
#     # print("A after", a)
#     if isNonDecreasing(a):
#         print("YES")
#     else:
#         print("NO")
# 4
# 1 4 2 3 - NO

# def deleteDuplicates(head):
#     list = []
#     for ele in head:
#         if ele not in list:
#             list.append(ele)
#         else:
#             while ele in list:
#                 list.remove(ele)
#     return list

# head = [1,2,3,3,4,4,5]
# print(deleteDuplicates(head))

nums1 = [0]
# print(sorted(nums))
# print(nums.sort())
# print(nums.index(2))

for x in range(len(nums1)-1,-1, -1):
    if nums1[x] == 0:
        nums1.pop(x)
    else:
        break
    print("iteracja", x)
print(nums1)