class Solution:
    def solve(self, board: List[List[str]]) -> None:
        width  = len(board[0])
        height = len(board)

        @cache
        def markborder(x, y):
            if x < 0 or x > width - 1:
                return
            if y < 0 or y > height - 1:
                return
            if board[y][x] != "O":
                return

            board[y][x] = "!"
            markborder(x-1, y)
            markborder(x+1, y)
            markborder(x, y-1)
            markborder(x, y+1)

        for y in range(height):
            markborder(0, y)
            markborder(width - 1, y)
        for x in range(width):
            markborder(x, 0)
            markborder(x, height - 1)

        for y in range(height):
            for x in range(width):
                if board[y][x] == "O":
                    board[y][x] = "X"
                if board[y][x] == "!":
                    board[y][x] = "O"
