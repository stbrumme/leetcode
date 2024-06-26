class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        # find smallest rectangle, similar to problem 3195
        @cache
        def one(x1, y1, x2, y2):
            # upper-left and lower-right corner
            a1 = b1 = +inf
            a2 = b2 = -inf

            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    if grid[y][x] == 1:
                        a1 = min(a1, x)
                        b1 = min(b1, y)
                        a2 = max(a2, x)
                        b2 = y
            return (a2 - a1 + 1) * (b2 - b1 + 1)

        @cache
        # try all splits into two parts
        def two(x1, y1, x2, y2):
            best = +inf

            # split horizontally and vertically
            for y in range(y1, y2):
                a = one(x1, y1,    x2, y)
                b = one(x1, y + 1, x2, y2)
                best = min(best, a + b)
            for x in range(x1, x2):
                a = one(x1,    y1, x,  y2)
                b = one(x + 1, y1, x2, y2)
                best = min(best, a + b)

            return best

        # split into two areas, split one of them again
        best = +inf

        x1 = y1 = 0
        x2 = width  - 1
        y2 = height - 1

        # split horizontally and vertically
        for y in range(y1, y2):
            a = one(x1, y1,    x2, y)
            b = two(x1, y + 1, x2, y2)
            best = min(best, a + b)
            a = two(x1, y1,    x2, y)
            b = one(x1, y + 1, x2, y2)
            best = min(best, a + b)
        for x in range(x1, x2):
            a = one(x1,    y1, x,  y2)
            b = two(x + 1, y1, x2, y2)
            best = min(best, a + b)
            a = two(x1,    y1, x,  y2)
            b = one(x + 1, y1, x2, y2)
            best = min(best, a + b)

        return best
