class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        # in the end only one value per column (condition 1)

        # process each column and compute changes, return array of size 10
        # (for each potential value)
        @cache
        def deeper(x):
            # count how much existing values need to be changed such that they are identical
            need = [ height ] * 10
            for y in range(height):
                need[grid[y][x]] -= 1

            # last column
            if x == width - 1:
                return need

            # compute column to the right
            next = deeper(x + 1)

            # minimize cost
            best = [ +inf ] * 10

            # all combinations of digits 0...9
            for one in range(10):
                for two in range(10):
                    if one != two: # condition 2
                        best[one] = min(best[one], need[one] + next[two])
            return best

        return min(deeper(0))
