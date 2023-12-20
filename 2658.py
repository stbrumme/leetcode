class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        result = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] > 0:
                    caught = 0
                    todo = [ (x, y) ]
                    seen = set()
                    while todo:
                        pos = todo.pop()
                        if pos in seen:
                            continue
                        seen.add(pos)

                        tx, ty = pos
                        caught += grid[ty][tx]
                        if tx > 0 and grid[ty][tx - 1]:
                            todo.append((tx - 1, ty))
                        if ty > 0 and grid[ty - 1][tx]:
                            todo.append((tx, ty - 1))
                        if tx < width - 1  and grid[ty][tx + 1]:
                            todo.append((tx + 1, ty))
                        if ty < height - 1 and grid[ty + 1][tx]:
                            todo.append((tx, ty + 1))

                    result = max(result, caught)

                    # not needed, but makes it quite a bit faster:
                    # replaced processed cells with land
                    for sx, sy in seen:
                        grid[sy][sx] = 0

        return result
