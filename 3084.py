class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        have = s.count(c)
        return (have + 1) * have // 2
