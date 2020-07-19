# https://leetcode.com/problems/3sum/
from typing import List

"""
Time Complexity:O(n^2) Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2)
This is asymptotically equivalent to O(n^2)
Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm. 
For the purpose of complexity analysis, we ignore the memory required for the output
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                print(nums, i, res,"before calling")
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        print(lo, hi,"values of lo and hi")
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            print("sum",sum)
            if sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]): # this second condition (lo > i + 1 and nums[lo] == nums[lo - 1]) is to skip if same element is repeated
                print(lo > i + 1)
                print(nums[lo] == nums[lo - 1])
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1


# [-5,-1,-1,0,0,0,6,6]