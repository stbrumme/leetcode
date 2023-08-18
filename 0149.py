class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        all = defaultdict(set)

        for p1 in range(len(points)):
            for p2 in range(p1 + 1, len(points)):
                x1 = points[p1][0]
                y1 = points[p1][1]
                x2 = points[p2][0]
                y2 = points[p2][1]

                dx = x1 - x2
                dy = y1 - y2

                # a = (y1-y2) / (x1-x2)
                # y = ax + b => b = y - ax
                a = float("inf")
                b = x1
                if dx != 0:
                    a = dy / dx
                    b = y1 - a * x1

                all[tuple([a, b])].add(p1)
                all[tuple([a, b])].add(p2)

        result = 0
        for a in all:
            result = max(result, len(all[a]))
        return result
