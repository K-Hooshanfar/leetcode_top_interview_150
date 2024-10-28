from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        max_profit = []

        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                j = i
            else:
                max_profit.append(prices[i] - prices[j])
                j += 1

        return sum(max_profit)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         pro=0
#         for i in range(1,len(prices)):
#             if prices[i]>prices[i-1]:
#                 pro+=prices[i]-prices[i-1]
#         return pro

# Example of how to run this:
nums = [1,2,3,4,5]

sol = Solution()
k = sol.maxProfit(nums)
print(f"Profit: {k}")