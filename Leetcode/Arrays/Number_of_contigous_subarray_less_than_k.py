def sumSubarrays(arr, target):
    out = 0
    total_sum = 0
    start = -1
    for i in range(len(arr)):
        total_sum += arr[i]
        print("total sum", total_sum)
        while(total_sum > target):
            print("in here")
            start += 1
            total_sum -= arr[start]
        out += i - start
        print(i, out)
    return out

nums = [1,2,3,0,3]
target = 3

print(sumSubarrays(nums, target))