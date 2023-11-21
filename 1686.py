class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        diffs = [ ( a, b ) for a, b in zip(aliceValues, bobValues) ]
        # pick largest values first (either boosts own value or prevents opponent from doing so)
        diffs.sort(reverse = True, key = lambda x : x[0] + x[1])

        result = 0
        player = 0 # alternate between 0 and 1
        for d in diffs:
            sign    = 1 - 2 * player # Alice +1, Bob -1
            result += d[player] * sign
            player ^= 1

        if result == 0:
            return 0
        return +1 if result > 0 else -1
