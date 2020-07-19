
def maxSubArraySum(a, size):
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        print("max ending here",max_ending_here)
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        print("max so far", max_so_far)
        if max_ending_here < 0:
            max_ending_here = 0
            print("max ending here if < 0 ", max_ending_here)
    return max_so_far


a = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArraySum(a, len(a)))