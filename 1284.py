class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat[0])
        n = len(mat)
        limit = m * n

        best = 99999
        for mask in range(1 << limit):
            if mask.bit_count() >= best:
                continue

            # deep copy
            grid = []
            for row in mat:
                grid.append(row.copy())

            # try all positions
            for bit in range(limit):
                if (1 << bit) & mask:
                    x = bit %  m
                    y = bit // m

                    grid[y][x] ^= 1
                    if x > 0:     grid[y][x-1] ^= 1
                    if x < m - 1: grid[y][x+1] ^= 1
                    if y > 0:     grid[y-1][x] ^= 1
                    if y < n - 1: grid[y+1][x] ^= 1

            total = 0
            for row in grid:
                total += sum(row)
            if total == 0:
                best = min(best, mask.bit_count())

        return best if best < 99999 else -1
