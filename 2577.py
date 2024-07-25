class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # there's one trick:
        # if we are stuck at a cell because all unvisited neighbors
        # have a timestamp which is too high,
        # then we return to the previous cell and return to the current cell again:
        # playing ping-pong ! this requires two steps per iteration.
        # if the difference is high then there's no need to actually perform the moves:
        # we will arrive at the next cell in an odd or even number of steps.
        height = len(grid)
        width  = len(grid[0])

        # obvious this fail in the very first step
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        todo   = [ ( 0, 0, 0 ) ]     # min-heap: timestamp, x, y
        deltas = ( 0, +1, 0, -1, 0 ) # compressed deltas
        while todo:
            now, x, y = heappop(todo)

            # arrived
            if x == width - 1 and y == height - 1:
                return now

            # placeholder, means "already visited"
            if grid[y][x] < 0:
                continue
            grid[y][x] = -1

            # need one unit to travel
            now += 1
            # hello neighbors !
            for dx, dy in zip(deltas, deltas[1 :]):
                nx = x + dx
                ny = y + dy

                if 0 <= nx < width and 0 <= ny < height:
                    arrive = max(now, grid[ny][nx])
                    # already seen
                    if arrive < 0:
                        continue

                    if arrive > now:
                        # need to wait
                        pingpong = arrive - now
                        arrive  += pingpong & 1

                    heappush(todo, ( arrive, nx, ny ))

        return -1 # never reached
