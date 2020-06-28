import math
def findSecondMaximum_usingsort(lst):
    lst.sort()
    return lst[-2]

def findSecondMaximum(lst):
    max = float('-inf')
    secondmax = float('-inf')
    for val in lst:
        if val > max:
            secondmax = max
            max = val
        elif val > secondmax:
            secondmax = val
    return secondmax


print(findSecondMaximum([4, 2, 1, 5, 0]))
print(findSecondMaximum([4]))

