from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                j = i
            else:
                max_profit = max(max_profit, prices[i] - prices[j])

        return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float("inf")
#         max_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#             elif prices[i] - min_price > max_profit:
#                 max_profit = prices[i] - min_price
#
#         return max_profit

# Example of how to run this:
nums = [2,4,1]

sol = Solution()
k = sol.maxProfit(nums)
print(f"Profit: {k}")
