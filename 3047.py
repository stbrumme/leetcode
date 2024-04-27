class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        result = 0 # store only one side, squared at the end

        rects = []
        for ( x1, y1 ), ( x2, y2 ) in zip(bottomLeft, topRight):
            rects.append(( x1, y1, x2, y2, min(x2 - x1, y2 - y1)))
        rects.sort()

        for i, ( x1, y1, x2, y2, s ) in enumerate(rects):
            # largest possible square
            if s <= result:
                continue

            for m1, n1, m2, n2, _ in rects[i + 1 :]:
                # no overlap or too small to produce a larger square
                if x2 - result <= m1:
                    break

                # extents
                x = min(x2, m2) - max(x1, m1)
                y = min(y2, n2) - max(y1, n1)
                square = min(x, y)
                result = max(result, square)

        return result ** 2
