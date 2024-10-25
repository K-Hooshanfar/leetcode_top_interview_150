from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1

        return i + 1



# Example of how to run this:
nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
k = sol.removeDuplicates(nums)
print(f"Length after removal: {k}")
print(f"Modified list: {nums[:k]}")