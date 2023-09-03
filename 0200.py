class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        unknown = set()
        for x in range(width):
            for y in range(height):
                if grid[y][x] != "0":
                    unknown.add(tuple([ x, y ]))

        result = 0
        visited = set()
        while unknown:
            result += 1
            todo = set([ unknown.pop() ])
            while todo:
                cell = todo.pop()
                x, y = cell

                if grid[y][x] == "0":
                    continue

                if cell in visited:
                    continue
                visited.add(cell)
                unknown.discard(cell)

                if x > 0:
                    todo.add(tuple([ x - 1, y ]))
                if x < width - 1:
                    todo.add(tuple([ x + 1, y ]))
                if y > 0:
                    todo.add(tuple([ x, y - 1 ]))
                if y < height - 1:
                    todo.add(tuple([ x, y + 1 ]))

        return result
