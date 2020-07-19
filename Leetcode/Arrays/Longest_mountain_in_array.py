# https://leetcode.com/problems/longest-mountain-in-array/

"""
Time Complexity: O(N), where N is the length of A.

Space Complexity: O(1)
"""

class Solution(object):
    def longestMountain(self, A):
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]:

                while end+1 < N and A[end] < A[end+1]:
                    end += 1
                print(A[end])
                if end + 1 < N and A[end] > A[end + 1]:
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    
                    print(A[end])
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans


# [1,2,1,4,5,6,3,2,9]