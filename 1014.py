class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # v[i] + v[j] + i - j = (v[i] + i) + (v[j] - j)
        # let's make     left =  v[i] + i                 <= almost fixed
        # and           right =               v[j] - j    <= for each j
        best = 0
        left = values[0] # v[i] + i for i = 0
        for j in range(1, len(values)):
            right = values[j] - j
            best  = max(best, left + right)
            # could be a new start, too, then i = j
            left  = max(left, values[j] + j)

        return best
