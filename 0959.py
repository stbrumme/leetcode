class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        width  = len(grid[0])
        height = len(grid)

        # each cell consists of four areas:
        #  \ 0 /
        #   \ /
        #  1 X 2
        #   / \
        #  / 3 \
        up    = 0
        left  = 1
        right = 2
        down  = 3

        # unique integer code for each cell
        def id(x, y, area):
            return x * 1000 + y * 10 + area # 1 <= x,y <= 30 according to problem constraints

        # union-find, copied from problem 721
        parent = {}
        # initially parent[a] = a
        for y in range(height):
            for x in range(width):
                for area in range(4):
                    i = id(x, y, area)
                    parent[i] = i

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

        # merge two cells, check if x2/y2 is valid (x1/y2 is assumed to be valid)
        def merge(x1, y1, area1, x2, y2, area2):
            if 0 <= x2 < width and 0 <= y2 < height:
                union(id(x1, y1, area1), id(x2, y2, area2))

        for y in range(height):
            for x in range(width):
                cell = grid[y][x]
                if cell == "/" or cell == " ":
                    merge(x, y, left,  x - 1, y, right)
                    merge(x, y, up,    x, y - 1, down)
                    merge(x, y, left,  x, y,     up)

                    merge(x, y, right, x + 1, y, left)
                    merge(x, y, down,  x, y + 1, up)
                    merge(x, y, right, x, y,     down)

                if cell == "\\" or cell == " ":
                    merge(x, y, left,  x - 1, y, right)
                    merge(x, y, down,  x, y + 1, up)
                    merge(x, y, left,  x, y,     down)

                    merge(x, y, right, x + 1, y, left)
                    merge(x, y, up,    x, y - 1, down)
                    merge(x, y, right, x, y,     up)

        unique = set()
        for y in range(height):
            for x in range(width):
                unique.add(find(id(x, y, up)))
                unique.add(find(id(x, y, left)))
                unique.add(find(id(x, y, right)))
                unique.add(find(id(x, y, down)))
        return len(unique)
