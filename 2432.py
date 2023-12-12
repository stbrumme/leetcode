class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        result  = 0
        longest = 0
        start   = 0
        for id, leave in logs:
            duration = leave - start
            if longest < duration or (longest == duration and result > id):
                longest = duration
                result  = id
            start = leave
        return result
