from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0  # farthest reachable index as we iterate through the list
        i = 0  # pointer to keep track of the current position

        while i <= j:  # loop as long as the current position is reachable
            j = max(j, i + nums[i])  # update the farthest reachable index
            if j >= len(nums) - 1:
                return True
            i += 1  # move to the next position

        return False

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goal= len(nums)-1
#
#         for i in range(len(nums)-2,-1,-1):
#             if i+nums[i]>=goal:
#                 goal=i
#
#         return True if goal==0 else False

nums1 = [0,2,3]

sol = Solution()
len = sol.canJump(nums1)
print(len)


# doesnt work

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#
#         j = 0
#         i = 0
#         for k in range(len(nums)):
#
#             if i >= len(nums) - 1:
#                 break
#
#             if k != len(nums)-1:
#                 # print(k)
#                 j = max(j, i + nums[i])
#                 i += 1
#
#         if j >= len(nums) - 1:
#             return True
#         else:
#             return False