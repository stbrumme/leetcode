class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1

        tick = -n # all tasks may start at first tick, without delay
        step = 10**8
        # encoding: timestamp, priority, ASCII
        def deadline(t):
            return (tick + n) * step + (len(tasks) - freq[t]) * 10**3 + ord(t)

        next = []
        for f in freq:
            heappush(next, deadline(f))

        tick = 0
        while next:
            tick += 1
            current = next[0]
            # nothing ready ?
            if current > tick*step:
                continue

            # ready task, highest priority
            which = chr(current % 1000)
            freq[which] -= 1
            if freq[which] == 0:
                heappop(next)
            else:
                heapreplace(next, deadline(which))

            # postpone other ready tasks
            while next and next[0] < tick*step:
                heappushpop(next, next[0] + step)

        return tick