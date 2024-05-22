class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        result = 0
        height = len(grid)
        width  = len(grid[0])

        # count all values
        have = defaultdict(int)
        for row in grid:
            for value in row:
                have[value] += 1

        # must have same modulo class
        modulo = grid[0][0] % x
        for h in have:
            if modulo != h % x:
                return -1

        # median
        need = (height * width) // 2
        median = 0
        for h in sorted(have):
            need -= have[h]
            if need < 0:
                median = h
                break

        # deviation from median
        for h in have:
            diff    = abs(h - median)
            result += diff * have[h]

        return result // x
