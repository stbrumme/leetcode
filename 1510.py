class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = set()
        for i in range(1, floor(n**0.5)):
            squares.add(i*i)

        @cache
        def deeper(stones):
            if stones == 0:
                return False

            if stones in squares:
                return True

            i = floor(sqrt(n)) # pick as many as possible
            while i > 0:
                if stones - i*i >= 0 and not deeper(stones - i*i):
                    return True
                i -= 1

            return False

        return deeper(n)
