class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        width  = len(board[0])
        height = len(board)

        deltas = [ [ -1, -1 ], [ -1, 0 ], [ -1, +1 ],
                   [  0, -1 ],            [  0, +1 ],
                   [ +1, -1 ], [ +1, 0 ], [ +1, +1 ] ]

        def count(x, y):
            result = 0
            for dx, dy in deltas:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < width and 0 <= yy < height:
                    if board[yy][xx] in [ "M", "X" ]:
                        result += 1
            return result

        def reveal(x, y):
            # detect mine
            if board[y][x] == "M":
                board[y][x] = "X"
                return

            # already visible
            if board[y][x] != "E":
                return

            # count mines
            board[y][x] = str(count(x, y))

            # reveal surrounding squares if blank
            if board[y][x] == "0":
                board[y][x] = "B"
                for dx, dy in deltas:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < width and 0 <= yy < height:
                        # recursion
                        reveal(xx, yy)

        reveal(click[1], click[0])
        return board
