from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Example of how to run this:
nums = [0,1,2,2,3,0,4,2]
val = 2

sol = Solution()
k = sol.removeElement(nums, val)
print(f"Length after removal: {k}")
print(f"Modified list: {nums[:k]}")