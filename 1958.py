class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        height = len(board)
        width  = len(board[0])

        # it took me a while to understand that we only need one good line
        # (out of at most 8 possible lines), the rest can be bad

        # return grid[y][x] or "." if out of bounds
        def get(x, y):
            if x < 0 or x >= width:
                return "."
            if y < 0 or y >= height:
                return "."

            return board[y][x]

        # 8 directions
        delta = [ [ -1, -1 ], [ 0, -1 ], [ +1, -1 ],
                  [ -1,  0 ],            [ +1,  0 ],
                  [ -1, +1 ], [ 0, +1 ], [ +1, +1 ] ]
        # check each direction
        for dx, dy in delta:
            # first point "in the middle"
            x = cMove + dx
            y = rMove + dy

            # must have opposite color
            have = get(x, y)
            if have == color or have == ".":
                continue

            need = have
            for step in range(2, 9):
                x += dx
                y += dy

                have = get(x, y)
                # finished too early
                if have == ".":
                    break

                # valid endpoint
                if have != need:
                    return True

        # not a single good line
        return False
