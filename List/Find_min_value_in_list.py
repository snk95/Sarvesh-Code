import math
def findMinimum_my_code(arr):
    min_value=math.inf
    if len(arr) ==0:
        return None
    for i in arr:
        min_value=min(min_value,i)
    return min_value

#O(n)
def findMinimum(lst):
    if (len(lst) <= 0):
        return None
    minimum = lst[0]
    for ele in lst:
        # update if found a smaller element
        if ele < minimum:
            minimum = ele
    return minimum

#O(nlogn)
def findMinimum_least_efficient(lst):
    if (len(lst) <= 0):
        return None
    lst.sort()  # sort list
    return lst[0]  # return first element


print(findMinimum([9, 2, 3, 6]))


print(findMinimum_my_code([]))
