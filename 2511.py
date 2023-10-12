class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # not clear from description whether all your forts may move at once or just one fort, the "best" fort
        # => it's the latter, making the problem much easier
        previous = -9 # just a number that's not in [ -1, 0, +1 ]
        captured = 0
        best     = 0
        for f in forts:
            if f == 0:
                captured += 1
            else:
                if f * previous == -1: # different sign, one is +1 and the other is -1
                    best = max(best, captured)

                captured = 0
                previous = f

        return best
