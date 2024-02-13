class Solution:
    def minLength(self, s: str) -> int:
        result = 0
        while result != len(s):
            result = len(s)
            s = s.replace("AB", "")
            s = s.replace("CD", "")
        return result
