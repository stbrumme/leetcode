class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        # grid's values => deltas for x and y
        signs = { 1: [ +1, 0 ], 2: [ -1, 0 ], 3: [ 0, +1 ], 4: [ 0, -1 ] }

        done = {}
        todo = [ (0, 0, 0) ] # min-heap cost,x,y
        while True:
            cost, x, y = heappop(todo)

            # already optimized ?
            if ( x, y ) in done:
                continue
            done[( x, y )] = cost

            # finish line
            if x == width - 1 and y == height - 1:
                print(done)
                return cost

            # process all four directions
            for direction in range(1, 4 + 1):
                dx, dy = signs[direction]
                nx = x + dx
                ny = y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if direction == grid[y][x]:
                        heappush(todo, ( cost,     nx, ny )) # follow the sign
                    else:
                        heappush(todo, ( cost + 1, nx, ny )) # modify sign
