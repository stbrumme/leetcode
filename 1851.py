class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = {}
        heapify(intervals)

        short = [] # min-heap storing the shortest intervals relevant for current query
        for q in sorted(queries):
            # add intervals overlapping the current query
            while intervals and intervals[0][0] <= q:
                left, right = heappop(intervals)
                heappush(short, ( right - left + 1, right ))

            # remove intervals when they are too far left
            while short and short[0][1] < q:
                heappop(short)

            # pick shortest
            if short:
                result[q] = short[0][0]

        return [ result.get(q, -1) for q in queries ]
