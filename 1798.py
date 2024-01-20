class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # simple code but took me a while ...

        # upper end of the range where we can make every number
        high = 0
        for c in sorted(coins):
            # if we look at the next coin, we can add c to all those numbers
            # that means we can add c to high, c to high - 1, c to high - 2, ...
            # in the end we extend our range from high to high + c

            # however, if c > high + 1 then there is no way to represent high + 1
            if c > high + 1:
                break

            high += c

        return high + 1 # including the zero
