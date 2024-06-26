class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        x1 = y1 = +inf # upper-left  corner
        x2 = y2 = 0    # lower-right corner

        for y in range(height):
            ones = 0
            for x in range(width):
                if grid[y][x] == 1:
                    x1 = min(x1, x)
                    x2 = max(x2, x)
                    ones += 1

            if ones > 0:
                y1 = min(y1, y)
                y2 = y

        return (x2 - x1 + 1) * (y2 - y1 + 1)
