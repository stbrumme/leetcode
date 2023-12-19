class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        width  = len(board[0])
        height = len(board)

        result = 0
        seen   = set()
        for y in range(height):
            for x in range(width):
                if (x, y) in seen:
                    continue

                seen.add((x, y))
                if board[y][x] == "X":
                    result += 1

                    sx = x
                    while sx < width - 1 and board[y][sx + 1] == "X":
                        sx += 1
                        seen.add((sx, y))
                    sy = y
                    while sy < height - 1 and board[sy + 1][x] == "X":
                        sy += 1
                        seen.add((x, sy))

        return result
