class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        height = len(grid)
        width  = len(grid[0])

        deltas = ( 0, +1, 0, -1, 0 ) # compressed deltas
        todo   = [ [ 0, 0, 0, 0 ] ]  # steps, removed, x, y
        seen   = {}                  # x, y = minimum removed

        while todo:
            steps, removed, x, y = heappop(todo)

            # arrived
            if x == width - 1 and y == height - 1:
                return steps

            # reject if a better way was already found
            best = seen.get(( x, y ), +inf)
            if removed >= best:
                continue
            seen[( x, y )] = removed

            for dx, dy in zip(deltas, deltas[1 :]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if grid[y][x] == 1:
                        # remove a wall
                        if removed < k:
                            heappush(todo, ( steps + 1, removed + 1, nx, ny ))
                    else:
                        # walk to a non-obstructed cell
                        heappush    (todo, ( steps + 1, removed,     nx, ny ))

        return -1
