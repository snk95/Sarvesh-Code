def findSum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False

# O(n ) and space O(n)
def findSum_my_code(lst, k):
    ans = list()
    d = dict()
    for i in lst:
        if k - i in d:
            ans.append((d[k - i], i))

        else:
            d[i] = i

    return ans

#solution three O(nlogn) logn for binary search
def binarySearch(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def findSum_binary_search(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binarySearch(lst, k - lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k - lst[j]]


print(findSum([1, 5, 3], 2))
print(findSum([1, 2, 3, 4], 5))

print(findSum([1,2,6,7],8))
print(findSum_my_code([1,2,6,7],8))