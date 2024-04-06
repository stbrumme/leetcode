class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # timestamp indicating how long to wait before processing a task of each ID
        wait = defaultdict(int)

        now = 0
        for t in tasks:
            now = max(now, wait[t]) + 1 # plus one: process it
            wait[t] = now + space

        return now
