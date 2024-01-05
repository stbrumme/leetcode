class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        result = 0

        high = 0 # highest flipped position so far
        for i, f in enumerate(flips, start = 1):
            high = max(high, f)
            if high == i:
                result += 1 # all flips happened "on the left side"

        return result
