class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        board = []
        for _ in range(n):
            board.append([0] * n)

        # initial position
        board[row][column] = 1

        # helper function
        def add(b, x, y, what):
            if 0 <= x < n and 0 <= y < n:
                b[y][x] += what

        for _ in range(k):
            next = []
            for _ in range(n):
                next.append([0] * n)

            for y in range(n):
                for x in range(n):
                    have = board[y][x]
                    add(next, x - 2, y - 1, have)
                    add(next, x + 2, y - 1, have)
                    add(next, x - 2, y + 1, have)
                    add(next, x + 2, y + 1, have)
                    add(next, x - 1, y - 2, have)
                    add(next, x + 1, y - 2, have)
                    add(next, x - 1, y + 2, have)
                    add(next, x + 1, y + 2, have)
            board = next

        total = sum(sum(r) for r in board)
        return total / 8 ** k
