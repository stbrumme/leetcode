class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hori = sorted(horizontalCuts + [ 0, h ])
        vert = sorted(verticalCuts   + [ 0, w ])

        x = y = 0
        for a, b in zip(hori, hori[1 :]):
            x = max(x, b - a)
        for a, b in zip(vert, vert[1 :]):
            y = max(y, b - a)

        return (x * y) % 1_000_000_007
