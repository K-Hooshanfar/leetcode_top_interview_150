from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies


candies  = [2,3,5,1,3]
extraCandies = 3
sol = Solution()
len = sol.kidsWithCandies(candies, extraCandies)
print(len)