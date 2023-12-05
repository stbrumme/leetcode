class Solution:
    def numberOfMatches(self, n: int) -> int:
        return 0 if n < 2 else n // 2 + self.numberOfMatches(n - (n // 2))
