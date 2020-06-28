def rightRotate_my_code(lst, n):
    n = n % len(lst)
    while n>0:
        a=lst.pop()
        lst.insert(0,a)
        n-=1
    return lst

#O(n) and space O(n)
def rightRotate(lst, n):
    n = n % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - n, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - n):
        rotatedList.append(lst[item])
    return rotatedList

#O(n)
def rightRotate_optimal(lst, n):
    # get rotation index
    n = n % len(lst)
    print(lst[-n:])

    return lst[-n:] + lst[:-n]

print(rightRotate([10, 20, 30, 40, 50], abs(3)))