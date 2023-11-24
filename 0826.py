class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # most profitable jobs first
        jobs = [ (-p, d) for p, d in zip(profit, difficulty) ] # max-heap
        heapify(jobs)

        # most skilled workers first
        result = 0
        for w in sorted(worker, reverse = True):
            while jobs and jobs[0][1] > w:
                heappop(jobs)

            if not jobs:
                break # a few workers will be unemployed

            p, d = jobs[0]
            result += -p # profit was negated for max-heap

        return result
