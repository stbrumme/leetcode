class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        # make room for positive island IDs
        water  = 0
        island = -1
        for y in range(height):
            for x in range(width):
                grid[y][x] -= 1

        # replace 0 with value
        def fill(x, y, value):
            todo = [ (x, y) ]
            while todo:
                x, y = todo.pop()
                if 0 <= x < width and 0 <= y < height and grid[y][x] == island:
                    grid[y][x] = value
                    todo.append((x - 1, y))
                    todo.append((x + 1, y))
                    todo.append((x, y - 1))
                    todo.append((x, y + 1))

        # remove islands on the border
        for x in range(width):
            fill(x,          0, water)
            fill(x, height - 1, water)
        for y in range(height):
            fill(0, y,         water)
            fill(width - 1, y, water)

        count = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == island:
                    count += 1
                    fill(x - 1, y, count)
                    fill(x + 1, y, count)
                    fill(x, y - 1, count)
                    fill(x, y + 1, count)

        return count
