class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        result = 0

        have = [ 0 ] * 24
        for h in hours:
            reduced = h % 24 if h >= 24 else h
            other   = 0 if reduced == 0 else 24 - reduced
            result += have[other]
            have[reduced] += 1

        return result
