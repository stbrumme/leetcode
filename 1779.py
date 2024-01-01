class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        best   = +inf
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                distance = abs(px - x) + abs(py - y)
                if distance < best:
                    result = i
                    best   = distance
        return result
