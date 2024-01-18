class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        result = 0

        # compute tasks in reverse order of how they will be finished:
        # first compute tasks where there is little overhead
        # that overhead isn't lost, it can be consumed by other tasks
        for actual, minimum in sorted(tasks, key = lambda x : x[1] - x[0]):
            result += actual
            if result < minimum:
                result = minimum

        return result
