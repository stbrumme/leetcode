class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        # start => end
        fromto = defaultdict(list)
        for i in intervals:
            start, end = i
            fromto[start].append(end)

        # reduce to at most one element starting at each point
        unique = { }
        result = 0
        for f in fromto:
            result   += len(fromto[f]) - 1
            unique[f] = min(fromto[f])

        # from left to right
        end = float("-inf")
        for start in sorted(unique):
            if start >= end:
                end = unique[start]
            else:
                # collision
                result += 1
                # choose the shorter interval
                end = min(end, unique[start])

        return result
