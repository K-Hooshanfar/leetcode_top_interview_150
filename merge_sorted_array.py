from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]

        for t in range(m):
            for i in range(m - 1):
                # print(A)
                if nums1[i] > nums1[i + 1]:
                    nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]

        for j in range(n):
            for t in range(m + j):
                if nums1[t] > nums2[j]:
                    nums1[t+1:m+j+1] = nums1[t:m+j]
                    nums1[t] = nums2[j]
                    break
                else:
                    nums1[m + j] = nums2[j]

            print(nums1)


# Example of how to run this:
nums1 = [1,2,3,0,0,0]
m = 3  # the number of initialized elements in nums1
nums2 = [2,5,6]
n = 3  # the number of elements in nums2

sol = Solution()
sol.merge(nums1, m, nums2, n)