# https://leetcode.com/problems/merge-intervals/
"""
Time complexity : O(nlogn) Other than the sort invocation, we do a simple linear scan of the list, so the runtime is
dominated by the O(nlgn) complexity of sorting
Space complexity : O(n)
"""

from typing import  List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


s=Solution()
print(s.merge([[1,3], [2,6], [6,7], [8,10], [10,18]]))