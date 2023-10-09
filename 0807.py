class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # highest building per row and column
        hx = [ 0 ] * n
        for y in range(n):
            for x in range(n):
                hx[x] = max(hx[x], grid[y][x])

        hy = [ 0 ] * n
        for x in range(n):
            for y in range(n):
                hy[y] = max(hy[y], grid[y][x])

        # do not exceed the highest building in the same row and column
        result = 0
        for y in range(n):
            for x in range(n):
                limit   = min(hx[x], hy[y])
                result += limit - grid[y][x]

        return result
