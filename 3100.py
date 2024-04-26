class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        result = empty = numBottles # drink all full bottles right away
        full = 0

        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            # turn empty into full bottles, and empty them immediately
            empty  += 1
            result += 1

        return result
