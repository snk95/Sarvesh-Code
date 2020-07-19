# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List
"""
Time O(n)
Space O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_length= len(prices)
        max_profit=0

        for i in range(1, prices_length):
            if prices[i] > prices[i-1]:
                max_profit = prices[i] - prices[i-1] + max_profit

        return max_profit
