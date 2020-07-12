import math
def findSecondMaximum_usingsort(lst):
    lst.sort()
    return lst[-2]

def findSecondMaximum(lst):
   if (len(lst) < 2):
       return
   # initialize the two to infinity
   max = second_max = float('-inf')
   for i in range(len(lst)):
       # update the max max if max value found
       if (lst[i] > max):
           second_max = max
           max = lst[i]
       # check if it is the second_max max and not equal to max
       elif (lst[i] > second_max and lst[i] != max):
           second_max = lst[i]
   if (second_max == float('-inf')):
       return
   else:
       return second_max


print(findSecondMaximum([4, 2, 1, 5, 0]))
print(findSecondMaximum([4]))

