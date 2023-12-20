class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        result = 0
        width  = len(grid[0])
        height = len(grid)

        # convert 1s to an ID and store the size of each island
        id      = 2   # start at 2 because 0 and 1 already used in grid
        islands = { } # size of each island, water has size 0 (simplifies code)
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    todo = [ (x, y) ]
                    have = set()
                    while todo:
                        tx, ty = todo.pop()
                        if (tx, ty) in have:
                            continue
                        have.add((tx, ty))
                        if tx > 0 and grid[ty][tx - 1] == 1:
                            todo.append(( tx - 1, ty ))
                        if ty > 0 and grid[ty - 1][tx] == 1:
                            todo.append(( tx, ty - 1 ))
                        if tx < width  - 1 and grid[ty][tx + 1] == 1:
                            todo.append(( tx + 1, ty ))
                        if ty < height - 1 and grid[ty + 1][tx] == 1:
                            todo.append(( tx, ty + 1 ))

                    # store size and ID
                    islands[id] = len(have)
                    for hx, hy in have:
                        grid[hy][hx] = id
                    id += 1

        # no islands yet => a new one will pop up with size 1
        if not islands:
            return 1
        if len(islands) == 1:
            # a single island, no bridges possible
            covered  = sum(islands.values())
            complete = width * height
            if covered == complete:
                return complete # cover the whole grid, don't change a cell
            else:
                return covered + 1

        result = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    bridging = set() # be careful with connecting an island with itself !
                    if x > 0:
                        bridging.add(grid[y][x - 1])
                    if y > 0:
                        bridging.add(grid[y - 1][x])
                    if x < width  - 1:
                        bridging.add(grid[y][x + 1])
                    if y < height - 1:
                        bridging.add(grid[y + 1][x])

                    # ignore water
                    bridging.discard(0)

                    total = 1          # current cell turns from water to land, too
                    for b in bridging: # and all distinct islands next to it
                        total += islands[b]

                    result = max(result, total)

        return result
