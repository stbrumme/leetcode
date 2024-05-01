class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        height = len(grid)
        width  = len(grid[0])

        limit  = max(queries)

        todo = [ ( grid[0][0], 0, 0 ) ] # min-heap of not-yet-seen cells
        seen = +inf                     # mark cell as visited
        jump = [[ 0, 0 ]]               # sorted list of potential query values and points gained

        # preprocess the whole grid
        steps = 0
        while todo:
            score, y, x = heappop(todo)

            # skip already visited cells
            if grid[y][x] == seen:
                continue
            grid[y][x] = seen

            # update scores / points
            steps += 1
            if score > jump[-1][0]:
                # new threshold
                jump.append([ score, steps ])
                if score > limit: # early exit: no query exceed this value
                    break
            else:
                # same threshold
                jump[-1][1] = steps # same as += 1

            # continue with neighbors
            def add(x, y):
                if 0 <= x < width and 0 <= y < height and grid[y][x] != seen:
                    heappush(todo, ( grid[y][x], y, x ))
            add(x - 1, y)
            add(x + 1, y)
            add(x, y - 1)
            add(x, y + 1)

        # and finally just look up results for each query
        for q in queries:
            pos = bisect_left(jump, [ q, 0 ])
            yield jump[pos - 1][1]
