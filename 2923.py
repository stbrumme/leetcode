class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i, g in enumerate(grid):
            # only 1's (and a zero at grid[i][i])
            if g[i] == 0 and g.count(1) == len(g) - 1:
                return i
