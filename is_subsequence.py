class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j = 0
        a = ""
        if s == "":
            return True

        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                # print(t[i])
                a += t[i]
                # print(a)
                if a == s:
                    return True
        return False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i = 0
#         j = 0
#
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#
#         return i == len(s)


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         j = 0  # Pointer for `s`
#
#         # If `s` is empty, it is always a subsequence
#         if s == "":
#             return True
#
#         # Traverse through `t`
#         for i in range(len(t)):
#             # If characters match, move pointer `j` for `s`
#             if t[i] == s[j]:
#                 j += 1
#                 # If `j` reaches the end of `s`, all characters have been matched
#                 if j == len(s):
#                     return True
#
#         # If we exit the loop and haven't matched all of `s`, return False
#         return j == len(s)


s = ""
t = "ahbgdc"

sol = Solution()
len = sol.isSubsequence(s, t)
print(len)
