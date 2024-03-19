class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0

        size = len(points)

        # a bit weird way to sort by x ascending and y descending:
        # flip sign of y, then sort, then flip back
        for p in points:
            p[1] *= -1
        points.sort()
        for p in points:
            p[1] *= -1

        for i in range(size):
            # upper-left
            x1, high = points[i]
            low      = -inf
            for j in range(i + 1, size):
                # lower-right
                x2, y2 = points[j]

                # no other point inside the rectangle
                if low < y2 <= high:
                    low     = y2 # shrink potential fence
                    result += 1

        return result
