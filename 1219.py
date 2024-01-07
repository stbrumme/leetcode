class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        def deeper(x, y):
            # outside
            if x < 0 or x >= width or y < 0 or y >= height:
                return 0
            # no gold, stop
            found = grid[y][x]
            if found == 0:
                return 0

            # take that gold
            grid[y][x] = 0

            # keep digging
            best =           deeper(x - 1, y)
            best = max(best, deeper(x + 1, y))
            best = max(best, deeper(x, y - 1))
            best = max(best, deeper(x, y + 1))

            # restore gold
            grid[y][x] = found

            return found + best

        result = 0
        for y in range(height):
            for x in range(width):
                result = max(result, deeper(x, y))
        return result
