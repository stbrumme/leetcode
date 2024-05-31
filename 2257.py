class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        height = m
        width  = n
        result = height * width - len(guards) - len(walls)

        # cell types (constants)
        empty   = 0
        visible = 1
        guard   = 2
        wall    = 3

        grid = [ [ empty ] * width for _ in range(height)]

        # add guards and walls
        for y, x in guards:
            grid[y][x] = guard
        for y, x in walls:
            grid[y][x] = wall

        # brute force: all four directions from each guard until hitting a border, a wall or another guard
        deltas = ( +1, 0, -1, 0, +1 )
        for y, x in guards:
            for dx, dy in zip(deltas, deltas[1 :]):
                sx = x + dx
                sy = y + dy

                while 0 <= sx < width and 0 <= sy < height and grid[sy][sx] <= visible: # empty = 0, visible = 1
                    # little branchless trick: subtract 1 if empty, subtract 0 if already guarded/visible
                    result -= 1 - grid[sy][sx]
                    grid[sy][sx] = visible

                    sx += dx
                    sy += dy

        return result
