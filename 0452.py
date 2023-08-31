class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1]) # sort by x_end

        pos = float("-inf")
        shots = 0
        for p in points:
            if pos < p[0]:
                shots += 1
                pos = p[1]

        return shots
