import collections

"""
Note that Python dictionaries do not maintain the order that elements were added to them so this solution will not 
necessarily display the FIRST non-repeating integer when traversing the dictionary! To get around this, we can use 
Python’s ordered dictionary as follows.
"""
def findFirstUnique(lst):
    orderedCounts = collections.OrderedDict()  # Creating an ordered dictionary
    # Initializing dictionary with pairs like (lst[i],0)
    orderedCounts = orderedCounts.fromkeys(lst, 0)
    print(orderedCounts)
    for ele in lst:
        orderedCounts[ele] += 1  # Incrementing for every repitition
    for ele in orderedCounts:
        if orderedCounts[ele] == 1:
            return ele
    return None


print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))
