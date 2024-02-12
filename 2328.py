class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])
        modulo = 1_000_000_007

        # get value of a cell, check bounds
        def get(x, y):
            if 0 <= x < width and 0 <= y < height:
                return grid[y][x]
            else:
                return 0 # smaller than any value

        @cache
        def deeper(x, y):
            value = grid[y][x]
            ways  = 1 # start new path here
            # continue with neighbors
            ways += deeper(x - 1, y) if get(x - 1, y) > value else 0
            ways += deeper(x + 1, y) if get(x + 1, y) > value else 0
            ways += deeper(x, y - 1) if get(x, y - 1) > value else 0
            ways += deeper(x, y + 1) if get(x, y + 1) > value else 0
            ways %= modulo
            return ways

        result = 0
        for y in range(height):
            for x in range(width):
                result += deeper(x, y)
        return result % modulo
