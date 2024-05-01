class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        result = 0
        height = len(grid)
        width  = len(grid[0])

        # sums per row and column
        rows = [ sum(r)   for r in grid ]
        cols = [ sum(r[c] for r in grid) for c in range(width) ]

        for y in range(height):
            for x in range(width):
                result += grid[y][x] * (cols[x] - 1) * (rows[y] - 1)

        return result
