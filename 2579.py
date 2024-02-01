class Solution:
    def coloredCells(self, n: int) -> int:
        # https://oeis.org/A001844
        n -= 1
        return 2 * n * (n + 1) + 1
