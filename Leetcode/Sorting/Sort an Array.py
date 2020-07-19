
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.divide(nums, 0, len(nums) - 1)

        return nums

    def divide(self, nums, lo, hi):

        if lo >= hi:
            return

        mid = (lo + hi) // 2 + 1

        self.divide(nums, lo, mid - 1)

        self.divide(nums, mid, hi)

        self.merge(nums, lo, mid, hi)

    def merge(self, nums, start1, start2, end2):
        p1 = start1
        p2 = start2
        curr = start1
        copy = nums[:]

        while curr <= end2:
            if p1 < start2 and p2 <= end2:
                if copy[p1] < copy[p2]:
                    nums[curr] = copy[p1]
                    p1 += 1

                else:
                    nums[curr] = copy[p2]
                    p2 += 1

            elif p1 < start2:
                nums[curr] = copy[p1]
                p1 += 1

            else:
                nums[curr] = copy[p2]
                p2 += 1

            curr += 1


