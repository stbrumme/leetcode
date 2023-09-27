class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        result = 0
        cost1, cost2 = max(cost1, cost2), min(cost1, cost2) # faster if cost1 is larger
        for one in range(0, total + 1, cost1):
            two = total - one
            result += 1 + two // cost2
        return result
