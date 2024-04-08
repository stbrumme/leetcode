class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        height = len(grid)
        width  = len(grid[0])

        done = []
        for y in range(height):
            done.append([ False ] * width)

        rings  = defaultdict(list)
        deltas = [ [ +1, 0 ], [ 0, +1 ], [ -1, 0 ], [ 0, -1 ] ]
        x = y  = direction = 0
        dx, dy = deltas[direction]
        level  = 1
        while not done[y][x]:
            rings[level].append(( x, y ))
            done[y][x] = True
            x += dx
            y += dy
            # change direction, potentially process next ring
            if x < 0 or y < 0 or x == width or y == height or done[y][x]:
                # undo
                x -= dx
                y -= dy
                # switch direction
                direction += 1
                # start new ring/level
                if direction == len(deltas):
                    direction = 0
                    level    += 1
                dx, dy = deltas[direction]
                x += dx
                y += dy

        # allocate memory
        result = []
        for y in range(height):
            result.append([ None ] * width)

        # process ring-by-ring
        for r in rings:
            size = len(rings[r])
            for one in range(size):
                two = (one + k) % size
                x,  y  = rings[r][one]
                gx, gy = rings[r][two]
                result[y][x] = grid[gy][gx]

        return result
