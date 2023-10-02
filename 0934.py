class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # find one island
        seedx, seedy = None, None
        for y in range(n):
            if seedx != None:
                break

            for x in range(n):
                if grid[y][x] == 1:
                    seedx = x
                    seedy = y
                    break

        two  = set()
        todo = set([ ( seedx, seedy ) ])
        while todo:
            next = set()
            for x, y in todo:
                if grid[y][x] == 0:
                    continue

                if (x, y) in two:
                    continue;
                two.add((x, y))
                grid[y][x] = 2

                if x > 0:
                    next.add((x - 1, y))
                if x < n - 1:
                    next.add((x + 1, y))
                if y > 0:
                    next.add((x, y - 1))
                if y < n - 1:
                    next.add((x, y + 1))

            todo = next

        # reduce to its beach (water next to land)
        beach = set()
        for x, y in two:
            if x > 0     and grid[y][x - 1] == 0:
                beach.add(( x - 1, y ))
            if x < n - 1 and grid[y][x + 1] == 0:
                beach.add(( x + 1, y ))
            if y > 0     and grid[y - 1][x] == 0:
                beach.add(( x, y - 1 ))
            if y < n - 1 and grid[y + 1][x] == 0:
                beach.add(( x, y + 1 ))

        # build bridges by covering beach
        steps = 0
        todo = beach
        while todo:
            next = set()

            for x, y in todo:
                if grid[y][x] == 1: # reached other island
                    return steps

                if grid[y][x] != 0:
                    continue

                grid[y][x] == 3 # build bridge

                if x > 0:
                    next.add((x - 1, y))
                if x < n - 1:
                    next.add((x + 1, y))
                if y > 0:
                    next.add((x, y - 1))
                if y < n - 1:
                    next.add((x, y + 1))

            todo   = next
            steps += 1
