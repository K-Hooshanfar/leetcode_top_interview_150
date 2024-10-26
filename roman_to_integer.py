class Solution:
    def romanToInt(self, s: str) -> int:

        dict = {'I': 1 ,
                'V': 5 ,
                'X': 10 ,
                'L': 50 ,
                'C': 100 ,
                'D': 500 ,
                'M': 1000 }
        real_number = 0
        i = 0
        while i +1 < len(s):
            if s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                real_number += dict[s[i+1]] - 1
                i += 2
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                real_number += dict[s[i + 1]] - 10
                i += 2
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                real_number += dict[s[i + 1]] - 100
                i += 2
            else:
                real_number += dict[s[i]]
                i += 1

        if i == len(s)-1:
            real_number += dict[s[i]]

        return real_number

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_map = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#
#         res = 0
#         for i in range(len(s)):
#             char = s[i]
#             if i < len(s) - 1 and roman_map[char] < roman_map[s[i+1]]:
#                 res -= roman_map[char]
#             else:
#                 res += roman_map[char]
#         return res

nums = 'MCMXCIV'

sol = Solution()
k = sol.romanToInt(nums)
print(f"number: {k}")
