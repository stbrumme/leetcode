class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [ 0 ] * m
        cols = [ 0 ] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        result = 0
        for y in range(m):
            for x in range(n):
                result += (rows[y] + cols[x]) & 1
        return result
