class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        # try a more efficient caching (instead of @cache):
        # grid has only positive numbers => use negative values to store a known result

        def deeper(x, y):
            if x == width - 1:
                return 0

            # known result
            value = grid[y][x]
            if value < 0:
                return -value

            best = 0
            # try all three options
            if y > 0          and grid[y - 1][x + 1] > value:
                best = max(best, 1 + deeper(x + 1, y - 1))
            if                    grid[y    ][x + 1] > value:
                best = max(best, 1 + deeper(x + 1, y))
            if y < height - 1 and grid[y + 1][x + 1] > value:
                best = max(best, 1 + deeper(x + 1, y + 1))

            grid[y][x] = -best
            return best

        return max(deeper(0, y) for y in range(height))
