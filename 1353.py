class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        result = 0

        heapify(events) # min-heap (start, end)
        active = []     # min-heap (end)

        now = 0
        while events or active:
            # next day
            now += 1
            if events and not active: # skip days if nothing's going on
                now = max(now, events[0][0])

            # events that just started
            while events and events[0][0] <= now:
                start, end = heappop(events)
                heappush(active, end)

            # remove expired
            while active and active[0] < now:
                heappop(active)

            # attend a meeting ending soon
            if active:
                result += 1
                heappop(active)

        return result
