def findFirstUnique(lst):
    d=list()
    for i in lst:
        if i not in d:
            d.append(i)
        else:
            d.remove(i)
    if d ==[]:
        return None
    return d[0]

print(findFirstUnique([9, 2, 3, 2, 9, 6, 6]))
print(findFirstUnique([]))