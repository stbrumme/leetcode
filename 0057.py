class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        pos = 0
        # outside, left => copy
        while pos < len(intervals) and intervals[pos][1] < newInterval[0]:
            result.append(intervals[pos])
            pos += 1

        # overlapping, left => merge
        while pos < len(intervals) and intervals[pos][0] < newInterval[0]:
            newInterval[0] = min(newInterval[0], intervals[pos][0])
            newInterval[1] = max(newInterval[1], intervals[pos][1])
            pos += 1

        # overlapping, right => merge
        while pos < len(intervals) and intervals[pos][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[pos][1])
            pos += 1

        result.append(newInterval)

        # outside, right => copy
        while pos < len(intervals):
            result.append(intervals[pos])
            pos += 1

        return result
