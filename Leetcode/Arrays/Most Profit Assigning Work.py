# https://leetcode.com/problems/most-profit-assigning-work/
from typing import List
"""
Time Complexity: O(N log N + Q log Q), where N is the number of jobs, and Q is the number of people. Note that i is not reset so time complexity 
is not Q*N
Space Complexity: O(N), the additional space used by jobs
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = zip(difficulty, profit)
        jobs = sorted(jobs)
        ans = i = best = 0

        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best

        return ans



s=Solution()
print(s.maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))
