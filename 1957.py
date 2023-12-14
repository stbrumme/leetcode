class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[:2]
        for i in range(2, len(s)):
            if s[i] != s[i - 2] or s[i] != s[i - 1]:
                result += s[i]
        return result
