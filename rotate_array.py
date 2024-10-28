from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(k):
            nums.insert(j, nums[-1])
            print(nums)
            nums.pop(-1)
            print(nums)


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k % n  # In case k is greater than n
#         # Reverse the entire array
#         nums.reverse()
#         # Reverse the first k elements
#         nums[:k] = reversed(nums[:k])
#         # Reverse the rest of the array
#         nums[k:] = reversed(nums[k:])


nums1 = [1,2,3,4,5,6,7]
k = 3

sol = Solution()
print(sol.rotate(nums1, k))