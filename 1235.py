class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        best = 0
        todo = [ (+inf, 0) ] # min-heap (end, profit), add a stop marker

        # process all jobs, ordered by startTime
        for s, e, p in sorted(zip(startTime + [ 10**10 ], endTime + [ 10**10 ], profit + [ 0 ])): # with stop marker, too
            # check all finished tasks
            while s >= todo[0][0]:
                end, profit = heappop(todo)
                best = max(best, profit)
            # including current job
            heappush(todo, (e, best + p))

        return best
