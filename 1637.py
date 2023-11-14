class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        have = sorted(set([ x for x,y in points ]))

        result = 0
        for i in range(1, len(have)):
            gap = have[i] - have[i - 1]
            result = max(result, gap)
        return result
