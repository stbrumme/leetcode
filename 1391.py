class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # union-find, copied from problem 721
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a]) # path compression
            return parent[a]

        # convert 2D to 1D
        def id(x, y):
            return 1000 * x + y

        # compatibility on the right  side of a cell
        horizontal = { 1: [ 1, 3, 5 ], 2: [], 3: [], 4: [ 1, 3, 5 ], 5: [], 6: [ 1, 3, 5 ] }
        # compatibility on the bottom side of a cell
        vertical   = { 1: [ ], 2: [ 2, 5, 6 ], 3: [ 2, 5, 6 ], 4: [ 2, 5, 6 ], 5: [], 6: [] }

        width  = len(grid[0])
        height = len(grid)
        # identity
        parent = {}
        for y in range(height):
            for x in range(width):
                i = id(x, y)
                parent[i] = i
        # merge compatible streets
        for y in range(height):
            for x in range(width):
                if x > 0:
                    left  = grid[y][x - 1]
                    right = grid[y][x]
                    if right in horizontal[left]:
                        union(id(x - 1, y), id(x, y))

                if y > 0:
                    up   = grid[y - 1][x]
                    down = grid[y    ][x]
                    if down in vertical[up]:
                        union(id(x, y - 1), id(x, y))

        # is there a path ?
        start  = id(0, 0)
        finish = id(width - 1, height - 1)
        return find(start) == find(finish)
