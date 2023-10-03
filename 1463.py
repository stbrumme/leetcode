class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])

        @cache
        def deeper(one, two, row):
            cherries = 0
            if one == two:
                cherries = grid[row][one]
            else:
                cherries = grid[row][one] + grid[row][two]

            if row == len(grid) - 1:
                return cherries

            best = 0
            for a in range(one - 1, one + 2):
                for b in range(two - 1, two + 2):
                    if 0 <= a < cols and 0 <= b < cols and a <= b:
                        best = max(best, deeper(a, b, row + 1))
            return cherries + best

        return deeper(0, cols - 1, 0)
