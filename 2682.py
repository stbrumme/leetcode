class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # compute everything zero-based, then convert to one-based
        turn = 1
        seen = [ 0 ] * n
        pos  = 0 # first player
        while True:
            seen[pos] += 1
            if seen[pos] == 2: # got the ball a second time
                break

            pos  += turn * k   # pass the ball
            pos  %= n          # wraparound
            turn += 1

        for i, s in enumerate(seen):
            if s == 0:
                yield i + 1 # convert to one-based
