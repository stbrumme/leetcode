class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        result = 0

        todo = defaultdict(int)
        todo[( startColumn, startRow )] = 1
        for _ in range(maxMove):
            next = defaultdict(int)
            for x, y in todo:
                current = todo[( x, y )]
                if 0 <= x < n and 0 <= y < m:
                    next[( x + 1, y)] += current
                    next[( x - 1, y)] += current
                    next[( x, y + 1)] += current
                    next[( x, y - 1)] += current
                else:
                    # copy paths already out of bounds
                    next[( x, y )] += current
            todo = next

        for x, y in todo:
            if x == -1 or x == n or y == -1 or y == m:
                result += todo[( x, y )]
        return result % 1_000_000_007
