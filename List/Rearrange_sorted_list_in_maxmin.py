def maxMin_myCode(lst):
    if len(lst) ==0:
        return
    elif len(lst) ==1:
        return lst

    left=0
    right=-1
    ans=[]
    count=0
    mid=len(lst) // 2
    while count <mid:
        ans.append(lst[right])
        ans.append(lst[left])
        left+=1
        right-=1
        count+=1
    if not len(lst) % 2 == 0:
        ans.append(lst[left])
    return ans

# O(n) and space O(1) but only works with non negative integers
def maxMin(lst):
    # Return empty list for empty list
    if (len(lst) == 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst

def maxMin_pythonic(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):
        # Append corresponding last element
        result.append(lst[-(i+1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2:
        # if middle value then append
        result.append(lst[len(lst)//2])
    return result

print(maxMin([1, 2, 3, 4, 5, 6, 7]))