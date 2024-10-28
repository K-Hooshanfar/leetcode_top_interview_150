import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        if s[::-1] == s:
            return True
        else:
            return False

nums1 = "A man, a plan, a canal: Panama"

sol = Solution()
len = sol.isPalindrome(nums1)
print(len)
