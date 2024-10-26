class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sep = s.split()
        return len(sep[-1])

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#
#         sep = s.split(" ")
#         while '' in sep:
#             sep.remove('')
#         last_len = len(sep[-1])
#
#         return last_len

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split().pop()) #pop removes and returns the last element in the list

# Example of how to run this:
nums1 = "Today is a nice day"
sol = Solution()
len = sol.lengthOfLastWord(nums1)
print(len)