class Solution:
    def minOperations(self, n: int) -> int:
        # https://oeis.org/A002620
        return (n * n) // 4
