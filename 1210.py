class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        size = len(grid)

        done = set()

        todo  = [ ( 1, 0, 0, 0 ) ] # (headx, heady, tailx, taily)
        steps = 0
        # straight-forward breadth-first search
        while todo:
            next = set()

            for snake in todo:
                # skip already known positions
                if snake in done:
                    continue
                done.add(snake)

                x, y, x2, y2 = snake

                # done
                if x == size - 1 and y == size - 1 and y == y2: # snake must be horizontal, too
                    return steps

                # too far right / down
                if x == size or y == size:
                    continue

                # helper function:
                # check if valid move, then add to list
                def add(x, y, x2, y2):
                    if 0 <= x < size and 0 <= y < size:
                        if grid[y][x] == 0 and grid[y2][x2] == 0:
                            next.add(( x, y, x2, y2 ))

                # move right
                add(x + 1, y, x2 + 1, y2)
                # move down
                add(x, y + 1, x2, y2 + 1)
                # rotate (x2 and y2 stay the same, but x2+1, y2+1 must be empty, too)
                if y2 + 1 < size and x2 + 1 < size and grid[y2 + 1][x2 + 1] == 0:
                    if y == y2:
                        # horizontal => vertical
                        add(x - 1, y + 1, x2, y2)
                    else:
                        # vertical   => horizontal
                        add(x + 1, y - 1, x2, y2)

            todo   = next
            steps += 1

        # running out of moves before reaching final position
        return -1
