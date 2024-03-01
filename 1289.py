class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # always choose the smallest value per row
        # except when it's in the same column, then choose the second smallest
        size = len(grid)
        best = [ (0, 0), (0, 0) ] # min-heap, two smallest sums yet
        for row in grid:
            # extract two smallest sums and their index
            low1, pos1 = heappop(best)
            low2       = best[0][0] # similar to heappop(best) but a tiny bit faster

            best.clear()
            for i, v in enumerate(row):
                next = v + (low2 if i == pos1 else low1)
                heappush(best, ( next, i ))

                # need at most 3 entries in our min-heap
                if len(best) > 3:
                    best.pop()

        return best[0][0]
