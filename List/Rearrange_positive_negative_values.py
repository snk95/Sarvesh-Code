def rearrange_mycode(lst):
    positive_list=[]
    for i in lst:
        if i >=0:
            positive_list.append(i)
        else:
            positive_list.insert(0,i)
    return positive_list

def reArrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if (lst[curr] < 0):
            # if not the last negative number
            if (curr is not leftMostPosEle):
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst

def reArrange_pythonic(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(reArrange([0, 0, 0, -2]))
print(reArrange([10, -1, 20, 4, 5, -9, -6]))