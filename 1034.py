class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        width  = len(grid[0])
        height = len(grid)

        # return color at x,y or -1 if out of bounds
        get = lambda x, y: grid[y][x] if 0 <= x < width and 0 <= y < height else -1

        todo   = [ [ col, row ] ]
        before = grid[row][col] # color used before painting it over
        border = set()
        seen   = set()
        while todo:
            x, y = todo.pop()
            if (x, y) in seen:
                continue
            seen.add((x, y))

            same = 0 # neighbors with same color
            if before == get(x - 1, y):
                todo.append((x - 1, y))
                same += 1
            if before == get(x, y - 1):
                todo.append((x, y - 1))
                same += 1
            if before == get(x + 1, y):
                todo.append((x + 1, y))
                same += 1
            if before == get(x, y + 1):
                todo.append((x, y + 1))
                same += 1

            # border if not fully surrounded by the same color
            if same < 4:
                border.add((x, y))

        # paint the border
        for x, y in border:
            grid[y][x] = color
        return grid
