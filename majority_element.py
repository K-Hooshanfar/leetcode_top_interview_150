from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return nums[0]
#
#         dic = {}
#         n = len(nums) // 2
#         for num in nums:
#             if num not in dic:
#                 dic[num] = 1
#             else:
#                 dic[num] += 1
#                 if dic[num] > n:
#                     return num



# Example of how to run this:
nums1 = [2,2,1,1,1,2,2,1,1]


sol = Solution()
candidate = sol.majorityElement(nums1)
print(candidate)