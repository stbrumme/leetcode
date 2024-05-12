class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        size = len(grid)

        # helper function, adds neighbors to a container, checks bounds
        delta = [ ( -1, 0 ), ( +1, 0 ), ( 0, -1 ), ( 0, +1 ) ]
        def add(container, x, y):
            for dx, dy in delta:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < size and 0 <= yy < size and grid[yy][xx] == 0:
                    container.add(( xx, yy ))

        # neighbors of 1s
        todo = set()
        for y in range(size):
            for x in range(size):
                if grid[y][x] == 1:
                    add(todo, x, y)

        # 1s are already in the grid, next safeness value is 2
        safeness = 2
        while todo:
            next = set()
            # set safeness, gather not-yet-processed neighbors
            for x, y in todo:
                if grid[y][x] == 0: # double-check it's a still unprocessed cell
                    grid[y][x] = safeness
                    add(next, x, y)

            # increase safeness level
            todo = next
            safeness += 1

        unknown = +inf
        best = []
        for y in range(size):
            best.append([ unknown ] * size)

        todo = [ ( -grid[0][0], 0, 0 ) ] # max-heap
        while todo:
            safeness, x, y = heappop(todo)
            safeness = -safeness

            # already got a better path
            if best[y][x] != unknown:
                continue

            # adjust
            safeness = min(safeness, grid[y][x])
            best[y][x] = safeness

            # early exit
            if x == y and y == size - 1:
                break

            # visit not-yet-seen neighbors, too
            for dx, dy in delta:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < size and 0 <= yy < size and best[yy][xx] == unknown:
                    heappush(todo, ( -safeness, xx, yy ) )

        return best[-1][-1] - 1
