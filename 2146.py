class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        # one of the more confusing problem statements ...
        result = []
        height = len(grid)
        width  = len(grid[0])

        low, high = pricing

        deltas = ( 0, +1, 0, -1, 0 )
        todo   = deque([ ( 0, start[0], start[1] ) ]) # steps, y, x
        while todo:
            steps, y, x = todo.popleft()

            # check if out of bounds
            if x < 0 or x == width or y < 0 or y == height:
                continue

            price = grid[y][x]
            if price == 0: # wall or already visited
                continue
            grid[y][x] = 0 # mark as visited

            # keep track of relevant items
            if low <= price <= high:
                result.append( ( steps, price, y, x ))

            # neighbors
            for dx, dy in zip(deltas, deltas[1 :]):
                todo.append(( steps + 1, y + dy, x + dx ))

        # sort by rank, emit first k
        for steps, price, y, x in sorted(result)[ : k]:
            yield y, x
