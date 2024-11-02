class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.strip()
#         return " ".join(reversed(s.split()))

t = "the sky is blue"

sol = Solution()
len = sol.reverseWords(t)
print(len)