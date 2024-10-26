from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i

# Example of how to run this:
nums = [0,0,1,1,1,1,2,3,3]

sol = Solution()
k = sol.removeDuplicates(nums)
print(f"Length after removal: {k}")
print(f"Modified list: {nums[:k]}")