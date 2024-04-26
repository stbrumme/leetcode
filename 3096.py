class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        size = len(possible)
        won  = possible.count(1)
        lost = size - won

        # assume that Bob plays all levels
        alice = 0
        bob   = won - lost

        # Bob must play at least the last level
        possible.pop()

        # Alice plays until she's better than Bob
        for i, p in enumerate(possible, 1):
            score  = 2 * p - 1 # convert [ 0, +1 ] to [ -1, +1 ]
            alice += score
            bob   -= score
            if alice > bob:
                return i

        return -1
