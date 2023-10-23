class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        for y in range(8):
            for x in range(8):
                if board[y][x] == "R":
                    for dx in range(x - 1, -1, -1):
                        if board[y][dx] == "p":
                            result += 1
                        if board[y][dx] != ".":
                            break
                    for dx in range(x + 1, 8):
                        if board[y][dx] == "p":
                            result += 1
                        if board[y][dx] != ".":
                            break
                    for dy in range(y - 1, -1, -1):
                        if board[dy][x] == "p":
                            result += 1
                        if board[dy][x] != ".":
                            break
                    for dy in range(y + 1, 8):
                        if board[dy][x] == "p":
                            result += 1
                        if board[dy][x] != ".":
                            break
        return result
