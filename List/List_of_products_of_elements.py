#Both are O(n)
def findProduct(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(findProduct([0, 1, 2, 3]))

def findProduct_my_code(arr):
    ans = []
    count = 0
    mul = 1
    for i in arr:
        if i == 0:
            count += 1
        else:
            mul = mul * i

    if count == 1:
        for i in arr:
            if i != 0:
                ans.append(0)
            else:
                ans.append(mul)
    elif count > 1:
        for i in arr:
            ans.append(0)

    else:
        for i in arr:
            ans.append(mul // i)

    return ans

print(findProduct([2,3,5]))
print(findProduct([2,3,0]))
print(findProduct([2,0,0]))