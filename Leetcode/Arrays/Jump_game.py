# https://leetcode.com/problems/jump-game/
from typing import  List

"""
Time O(n) 
Space O(1)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable_index = 0
        list_length = len(nums)

        for i in range(list_length):

            if i > reachable_index:
                return False

            elif reachable_index >= list_length - 1:
                return True

            reachable_index = max(reachable_index, nums[i] + i)

nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]
s= Solution()
print(s.canJump(nums))



