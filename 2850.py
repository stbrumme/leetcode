class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        @cache
        def deeper(board):
            # final board
            if board == "111111111":
                return 0

            best = +inf
            for a, have in enumerate(board):
                # found a stone we can/should move
                if have > "1":
                    have = str(int(have) - 1) # decrement counter
                    x1 = a %  3
                    y1 = a // 3

                    for b, need in enumerate(board):
                        if need == "0":
                            # replace a zero by one
                            next = board[ : b] + "1"  + board[b + 1 :]
                            # and decrement counter of current cell
                            next = next [ : a] + have + next [a + 1 :]

                            # process next stone
                            x2 = b %  3
                            y2 = b // 3
                            cost = abs(x1 - x2) + abs(y1 - y2)
                            best = min(best, deeper(next) + cost)
            return best

        # represent board as a simple string
        # abc
        # def
        # ghi
        # => "abcdefghi"
        initial = ""
        for y in range(3):
            for x in range(3):
                initial += str(grid[y][x])
        return deeper(initial)
