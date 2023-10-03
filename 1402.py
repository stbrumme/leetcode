class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        best = 0
        while satisfaction:
            total = 0
            for i, s in enumerate(satisfaction):
                total += (i + 1) * s
            best = max(best, total)

            del satisfaction[0]

        return best
