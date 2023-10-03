class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        all = sorted([ a, b, c ])
        low = 0
        if all[1] - all[0] != 1: # move closer to middle
            low += 1
        if all[2] - all[1] != 1: # move closer to middle
            low += 1
        if all[2] - all[1] == 2 or all[1] - all[0] == 2: # move between the other two
            low  = 1

        high = all[2] - all[0] - 2
        return [ low, high ]
