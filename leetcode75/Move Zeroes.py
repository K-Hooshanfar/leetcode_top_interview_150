from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                n -= 1
            else:
                i += 1
        print(nums)




candies  = [0,0,1]
sol = Solution()
len = sol.moveZeroes(candies)
print(len)

# for i in range(len(nums) - 1, -1, -1):  # Iterate backwards

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         slow = 0
#         for fast in range(len(nums)):
#             if nums[fast] != 0:
#                 nums[fast], nums[slow] = nums[slow], nums[fast]
#                 slow += 1

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)  # Get the initial size of the list
#         skip = 0  # To account for shifted indices when elements are popped
#
#         for i in range(n):
#             # Adjust for previously shifted elements
#             current_index = i - skip
#
#             if nums[current_index] == 0:
#                 nums.append(0)  # Append a zero to the end
#                 nums.pop(current_index)  # Remove the zero at the current position
#                 skip += 1  # Increment the skip count to compensate for pop