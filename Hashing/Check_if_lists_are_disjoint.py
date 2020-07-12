def is_disjoint(list1, list2):
    s = set(list1)  # Create set of list1 elements
    # iterate list 2
    for elem in list2:
        # if element in list1 then return False
        if elem in s:
            return False
    # Return True if no common element
    return True


list1 = [9, 4, 3, 1, -2, 6, 5]
list2 = [7, 10, 8]
list3 = [1, 12]
print(is_disjoint(list1, list2))
print(is_disjoint(list1, list3))
