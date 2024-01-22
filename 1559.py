class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        width  = len(grid[0])
        height = len(grid)

        deltas = [ +1, 0, -1, 0 ] # compact encoding of (0,1),(1,0),(0,-1),(-1,0)
        known  = set()            # visited cells

        # if we avoid the last cell then any time we visit an already known cell there is a cycle of length 4 or more
        def deeper(x, y, oldx = -1, oldy = -1): # True if cycle found
            if (x, y) in known:
                return True # cycle found
            known.add(( x, y ))

            dx = dy = 0
            for d in deltas:
                dy = dx
                dx = d

                nx = x + dx
                ny = y + dy
                # avoid stepping back => that would be a "cycle" of length 2, which is allowed
                if nx == oldx and ny == oldy:
                    continue

                # same color, respect borders
                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == grid[y][x]:
                    if deeper(nx, ny, x, y):
                        return True

            # no cycle (yet)
            return False

        # start at each (unknown) cell
        for y in range(height):
            for x in range(width):
                if (x, y) not in known and deeper(x, y):
                    return True

        return False
