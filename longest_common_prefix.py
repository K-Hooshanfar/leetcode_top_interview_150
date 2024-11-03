from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs or not strs[0]:
            return ""

        a = ""

        min_len = min(len(s) for s in strs)

        if min_len == 0:
            return ""

        for i in range(len(strs)-1):
            if strs[i][0] != strs[i+1][0]:
                return ""

        for i in range(min_len):
            current_char = strs[0][i]
            j = 1
            while j < len(strs):
                if strs[j][i] != current_char:
                    return a
                j += 1

            a += current_char

        return a


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         shortest_len = min(len(s) for s in strs)
#
#         for i in range(shortest_len):
#             char = strs[0][i]
#             for string in strs[1:]:
#                 if string[i] != char:
#                     return string[:i]


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#
#         res = ""
#         strs.sort()
#
#         for i in range(min(len(strs[0]), len(strs[-1]))):
#             if strs[0][i] == strs[-1][i]:
#                 res += strs[0][i]
#             else:
#                 return res
#
#         return res


solution = Solution()
print(solution.longestCommonPrefix(["abab", "aba", ""]))  # Output: ""
print(solution.longestCommonPrefix(["", ""]))  # Output: ""
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""