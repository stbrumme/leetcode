class Solution:
    def twoEggDrop(self, n: int) -> int:
        # https://oeis.org/A002024
        return int(sqrt(2 * n) + 0.5)
