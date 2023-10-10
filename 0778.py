class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        level = grid[0][0]
        todo  = [ ( level, 0, 0 ) ] # min-heap
        seen  = set()
        while True:
            l, x, y = heappop(todo)

            if ( x, y ) in seen:
                continue
            seen.add(( x, y ))

            level = max(level, l)
            if x == n - 1 and y == n - 1:
                return level

            if x > 0     and ( x - 1, y ) not in seen:
                heappush(todo, ( grid[y][x - 1], x - 1, y ))
            if x < n - 1 and ( x + 1, y ) not in seen:
                heappush(todo, ( grid[y][x + 1], x + 1, y ))
            if y > 0     and ( x, y - 1 ) not in seen:
                heappush(todo, ( grid[y - 1][x], x, y - 1 ))
            if y < n - 1 and ( x, y + 1 ) not in seen:
                heappush(todo, ( grid[y + 1][x], x, y + 1 ))
