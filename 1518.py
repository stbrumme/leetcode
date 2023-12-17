class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        full   = numBottles
        empty  = 0
        # no fancy math, just simulation
        while full > 0 or empty >= numExchange:
            if full > 0:
                result += 1
                full   -= 1
                empty  += 1
            if empty >= numExchange:
                full   += 1
                empty  -= numExchange
        return result
