class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        # compact representation of four directions
        deltas = ( 0, +1, 0, -1, 0 )

        # player
        px = py = 0
        # box
        bx = by = 0
        # target
        tx = ty = 0

        # alls cells within bounds and not being a wall
        valid = set()

        # locate these three points
        for y in range(height):
            for x in range(width):
                cell = grid[y][x]
                if   cell == "S":
                    px = x
                    py = y
                elif cell == "B":
                    bx = x
                    by = y
                elif cell == "T":
                    tx = x
                    ty = y

                if cell != "#":
                    valid.add(( x, y ))

        seen = set()                       # avoid loops
        todo = set([ ( px, py, bx, by ) ]) # position of player and box
        next = set()                       # push once more
        push = 0                           # number of pushes in "todo" (push + 1 in "next")
        while todo or next:
            # need one more push
            if not todo:
                todo  = next
                next  = set()
                push += 1

            px, py, bx, by = todo.pop()

            # move player
            for dx, dy in zip(deltas, deltas[1 :]):
                x = px + dx
                y = py + dy

                # check walls / out-of-bounds
                if (x, y) not in valid:
                    continue

                if x == bx and y == by:
                    # push box
                    bbxx = bx + dx
                    bbyy = by + dy

                    # done
                    if bbxx == tx and bbyy == ty:
                        return push + 1

                    # move box only if cell is free
                    id = ( x, y, bbxx, bbyy )
                    if ( bbxx, bbyy ) in valid and id not in seen:
                        next.add(id)
                else:
                    # just move player
                    id = ( x, y, bx, by )
                    if id not in seen:
                        todo.add(id)
                        seen.add(id)

        # failed
        return -1
