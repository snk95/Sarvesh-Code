#O(N) runtime & O(1) space
def containerMostWater(arr):
    if len(arr) < 2:
        return -1

    start = 0
    end = len(arr) - 1
    max_prod = float('-inf')

    while (start < end):
        prod = min(arr[start], arr[end]) * (end - start)
        max_prod = max(max_prod, prod)
        if arr[start] > arr[end]:
            end -= 1
        else:
            start += 1

    return max_prod


arr= [1,8,6,2,5,4,8,3,7]
arr1= [1,10,6,2,5,4,8,10,7]
print(containerMostWater(arr))
print(containerMostWater(arr1))