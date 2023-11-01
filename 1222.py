class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        hashed = set(tuple([ qx, qy ]) for qx, qy in queens) # faster than linear search
        deltas = [ [ -1, -1 ], [ -1, 0 ], [ -1, +1 ],\
                   [  0, -1 ],            [  0, +1 ],\
                   [ +1, -1 ], [ +1, 0],  [ +1, +1 ] ]

        kx, ky = king
        for dx, dy in deltas:
            for i in range(1, 8):
                qx = kx + dx * i
                qy = ky + dy * i
                if (qx, qy) in hashed:
                    yield [ qx, qy ]
                    break
                if min(qx, qy) < 0 or max(qx, qy) >= 8:
                    break # out of bounds
