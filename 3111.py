class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        result = 0

        covered = -1 # all points with x <= covered are already part of a rectangle
        for x, y in sorted(points): # y doesn't matter
            if x > covered:
                covered = x + w
                result += 1

        return result
