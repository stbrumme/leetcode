class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        result = +inf

        points.sort()
        all = set([ ( x, y ) for x, y in points ])

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1 : ], i + 1):
                # side a
                dx1 = x2 - x1
                dy1 = y2 - y1
                if max(dx1, dy1) >= result: # early exit
                    continue

                for x3, y3 in points[j + 1 : ]:
                    # side b
                    dx2 = x3 - x2
                    dy2 = y3 - y2
                    if max(dx2, dy2) >= result: # early exit
                        continue

                    # dot product is zero iff right angle
                    if dx1 * dx2 + dy1 * dy2 == 0:
                        # conclude fourth point
                        x4 = x3 - dx1
                        y4 = y3 - dy1
                        if ( x4, y4 ) in all:
                            # sqrt(a) * sqrt(b) = sqrt(a * b)
                            a = dx1 * dx1 + dy1 * dy1
                            b = dx2 * dx2 + dy2 * dy2
                            result = min(result, a * b) # defer final sqrt

        return 0 if result == +inf else sqrt(result)
