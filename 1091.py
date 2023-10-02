class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        deltas = [ (-1, -1), (-1, 0), (-1, +1),
                   ( 0, -1),          ( 0, +1),
                   (+1, -1), (+1, 0), (+1, +1) ]

        length = 1
        have = set()
        todo = set([( 0, 0 )])
        while todo:
            next = set()
            for x, y in todo:
                # done
                if x == n - 1 and y == n - 1:
                    return length

                # avoid loops
                if (x, y) in have:
                    continue
                have.add((x, y))

                # all eight directions
                for dx, dy in deltas:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < n and 0 <= yy < n and grid[yy][xx] == 0:
                        next.add(( xx, yy ))

            length += 1
            todo    = next

        return -1
