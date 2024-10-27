class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         n, h =len(needle),len(haystack)
#         for i in range(h-n+1):
#             if haystack[i:i+n] == needle:
#                 return i
#         return -1

haystack = "Hello"
needle = "ll"
sol = Solution()
len = sol.strStr(haystack, needle)
print(len)