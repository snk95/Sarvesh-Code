# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        track = dict()

        for i in range(len(nums)):
            if target - nums[i] in track:
                return [track[target - nums[i]], i]

            track[nums[i]] = i

        return []

