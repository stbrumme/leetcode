class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # solve the problem in reverse order:
        # initially everything is flooded, then land re-appears
        # stop as soon as top is connected to bottom

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # each day is connected only to itself (being its own parent)
        parent = { i: i for i in range(1, len(cells) + 1) }
        # special IDs
        top    = 888_888
        bottom = 999_999
        parent[top]    = top
        parent[bottom] = bottom

        # north, south, west, east
        directions = [ [ +1, 0, ], [ -1, 0], [ 0, +1 ], [ 0, -1 ] ]
        # cells which already became land
        have = {}
        day  = len(cells)
        for y, x in reversed(cells):
            have[(x, y)] = day
            # union with neighbors (if land)
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if (nx, ny) in have:
                    # merge those two days
                    next = have[(nx, ny)]
                    union(day, next)

            # touching north/south border
            if   y == 1:
                union(day, top)
            elif y == row:
                union(day, bottom)

            # connected ?
            if find(top) == find(bottom):
                break

            # still no bridge, keep going
            day -= 1

        return day - 1
