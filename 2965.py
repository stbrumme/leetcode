class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n     = len(grid)
        have  = set()
        need  = set(range(1, n * n + 1))
        twice = 0
        for row in grid:
            for r in row:
                if r in have:
                    twice = r
                have.add(r)
                need.discard(r)
        return [ twice, need.pop() ]
