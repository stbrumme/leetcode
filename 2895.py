class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # each CPU has 4 cores
        processorTime += processorTime
        processorTime += processorTime

        processorTime.sort()
        tasks.sort(reverse = True)
        # assign longest tasks to processors which are available early
        finish = 0
        for p, t in zip(processorTime, tasks):
            finish = max(finish, p + t)

        return finish
