class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        result = 0
        three  = 1
        for c in sorted(cost, reverse = True):
            if three < 3:
                result += c
                three  += 1
            else:
                three   = 1
        return result
