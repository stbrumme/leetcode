class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1 > bx1:
            ax1, bx1 = bx1, ax1
            ay1, by1 = by1, ay1
            ax2, bx2 = bx2, ax2
            ay2, by2 = by2, ay2

        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)

        if ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2:
            return a + b

        cx = max(ax1, bx1) - min(ax2, bx2)
        cy = max(ay1, by1) - min(ay2, by2)
        c  = cx * cy

        return a + b - c
