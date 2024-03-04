class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result = +inf
        # the second bot must "switch lanes" either at column 0 or n - 1
        first  = sum(grid[0]) # upper row, decreasing
        second = 0            # lower row, increasing
        for a, b in zip(grid[0], grid[1]): # switch lanes
            first  -= a
            result = min(result, max(first, second))
            second += b

            if second > result:
                break # early exit

        return result
