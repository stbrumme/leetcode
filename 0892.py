class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        def get(x, y):
            if 0 <= x < width and 0 <= y < height:
                return grid[y][x]
            return 0

        result = 0
        for y in range(height):
            for x in range(width):
                if get(x, y) == 0:
                    continue

                result += 2 # top and bottom
                # four sides, only if taller than neighbors
                result += max(0, get(x, y) - get(x - 1, y))
                result += max(0, get(x, y) - get(x + 1, y))
                result += max(0, get(x, y) - get(x, y - 1))
                result += max(0, get(x, y) - get(x, y + 1))

        return result
