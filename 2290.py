class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        # least number of walls removed to reach a cell
        # tricky use of extra cells to avoid out of bounds
        best   = [ [ +inf ] * width + [ -1 ] for _ in range(height) ]
        best  += [ [ -1   ] * width ]
        best[0][0] = 0

        deltas = ( 0, +1, 0, -1, 0 )
        # two parts: front elements removed one less wal than back elements
        todo   = [( 0, 0 )]
        more   = []
        while True:
            # need to tear down at least one more wall
            if not todo:
                todo = more
                more = []

            x, y  = todo.pop()
            walls = best[y][x]

            # reached the goal
            if x == width - 1 and y == height - 1:
                return walls

            for dx, dy in zip(deltas, deltas[1 :]):
                xx = x + dx
                yy = y + dy

                # track only if better than before
                if walls < best[yy][xx]:
                    if grid[yy][xx] == 0:
                        # no wall
                        todo.append(( xx, yy ))
                        best[yy][xx] = walls
                    else:
                        # remove wall
                        next = walls + 1
                        if next < best[yy][xx]:
                            more.append(( xx, yy ))
                            best[yy][xx] = next
