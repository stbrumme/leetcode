class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x = m
        y = n
        for ox, oy in ops:
            x = min(x, ox)
            y = min(y, oy)
        return x*y
