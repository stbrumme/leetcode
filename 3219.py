class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        result = 0

        # optimized version of problem 3218

        all = horizontalCut + [ -v for v in verticalCut ] # sign encodes orientation

        h = v = 0 # number of cuts
        for cost in sorted(all, key = lambda x : -abs(x)): # most expensive first
            if cost > 0:
                result +=  cost * (v + 1)
                h      += 1
            else:
                result += -cost * (h + 1) # was negated
                v      += 1

        return result
