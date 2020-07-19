"""Time complexity : O(N). Although there are nested loops, the inner loop is bounded to be run at most k times globally.
Together with the outer loop, we have the exact (N + k) number of operations. Since 0 < k ≤ N, the time complexity of
the main loop is bounded within 2N. For the logic outside the main loop, it is clear to see that their time complexity is
O(N). As a result, the overall time complexity of the algorithm is O(N)

Space complexity : O(N). We have a stack which would hold all the input digits in the worst case.
"""
class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []

        for num in nums:
            while (stack and k and int(stack[-1]) > int(num)):
                stack.pop()
                k = k - 1

            stack.append(num)

        if k:
            stack = stack[:-k]

        cur = 0

        while (cur < len(stack) and stack[cur] == '0'):
            cur += 1

        stack = stack[cur:]

        return "".join(stack) or '0'

