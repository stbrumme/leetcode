class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        result   = 0
        one      = 0  # highest value of all finished (single) courses
        finished = [] # min-heap of end-date of started courses
        for start, end, value in sorted(events):
            # process all finished courses, pick the highest valued
            while finished and finished[0][0] < start:
                endOne, valueOne = heappop(finished)
                one = max(one, valueOne)

            # "connect" the highest valued with current course
            result = max(result, one + value)

            # add current course to list of started courses
            heappush(finished, ( end, value ))

        return result
