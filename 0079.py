class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def deeper(x, y, pos):
            current = word[pos]
            if board[y][x] != current:
                return False

            if pos == len(word) - 1:
                return True

            # footprints
            board[y][x] = ":"

            if x > 0               and deeper(x - 1, y, pos + 1):
                return True
            if x < len(board[y])-1 and deeper(x + 1, y, pos + 1):
                return True
            if y > 0               and deeper(x, y - 1, pos + 1):
                return True
            if y < len(board)-1    and deeper(x, y + 1, pos + 1):
                return True

            # no more footprints
            board[y][x] = current
            return False

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == word[0] and deeper(x, y, 0):
                    return True

        return False
