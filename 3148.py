class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        # let's roll our own cache
        below   = [ -inf ] * width
        current = [ -inf ] * width

        # start at each cell, beginning in lower-right corner
        result = -inf
        for y in reversed(range(height)):
            have = 0
            for x in reversed(range(width)):
                score = -inf

                # right
                right = have
                have  = grid[y][x]
                if x < width - 1:
                    score = right - have + max(current[x + 1], 0)
                # down
                if y < height - 1:
                    next  = grid[y + 1][x]
                    score = max(score, next - have + max(below[x], 0))

                current[x] = score
                result = max(result, score)

            below = current

        return result
