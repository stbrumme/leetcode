class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        length = 0 # number of consecutive days
        last   = 0 # previous price

        for p in prices:
            # new "streak"
            if p != last - 1:
                length = 0

            # more or less triangle numbers
            length += 1
            result += length
            last    = p

        return result
