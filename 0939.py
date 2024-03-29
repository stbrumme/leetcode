class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        result = +inf

        # set up groups for each x- and y-value
        horizontal = defaultdict(set)
        vertical   = defaultdict(set)
        for x, y in points:
            horizontal[y].add(x)
            vertical  [x].add(y)

        # choose the smaller group to speed up the algorithm
        # (each would work, this is for performance reasons only)
        groups = vertical if len(vertical) < len(horizontal) else horizontal
        size = len(groups)

        candidates = sorted(groups)
        for i in range(size):
            for j in range(i + 1, size):
                a1 = candidates[i]
                a2 = candidates[j]
                a  = a2 - a1
                # look for identical x-values
                both = sorted(groups[a1] & groups[a2])
                # minimum rectangles
                if len(both) >= 2:
                    b = min([ b2 - b1 for b1, b2 in zip(both, both[1 :]) ])
                    result = min(result, a * b)

        return result if result != +inf else 0
