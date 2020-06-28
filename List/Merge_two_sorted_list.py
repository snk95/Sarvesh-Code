def merge_lists(lst1, lst2):
    ind1 = 0
    ind2 = 0
    while(ind1 < len(lst1) and ind2 < len(lst2)):
        if(lst1[ind1] > lst2[ind2]):
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1

    if(ind2 < len(lst2)):
        lst1.extend(lst2[ind2:])
    return lst1


def merge_lists_my_code(lst1, lst2):
    count1 = 0
    count2 = 0
    ans = []

    while count1 < len(lst1) and count2 < len(lst2):
        if lst1[count1] <= lst2[count2]:
            ans.append(lst1[count1])
            count1 += 1
        elif lst1[count1] > lst2[count2]:
            ans.append(lst2[count2])
            count2 += 1

    while count1 < len(lst1):
        ans.append(lst1[count1])
        count1 += 1
    while count2 < len(lst2):
        print("in here")
        ans.append(lst2[count2])
        count2 += 1

    return ans

print(merge_lists([1, 3, 4, 5],[2, 6, 7, 8]))