def findSum(lst, k):
    foundValues = {}
    for ele in lst:
        # Check for value in dictionary
        # If found return
        try:
            foundValues[k - ele]
            return [k - ele, ele]

        except KeyError:
            foundValues[ele] = 0

    return "No numbers add upto k"


def findSum_using_set(lst, value):
    foundValues = set()
    for ele in lst:
        if value - ele in foundValues:
            return [value-ele, ele]

        foundValues.add(ele)
    return False






print(findSum([1, 3, 2, 4], 6))
print(findSum_using_set([1, 3, 2, 4], 6))
