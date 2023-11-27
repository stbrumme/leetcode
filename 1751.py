class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        @cache
        def deeper(pos, attended):
            if pos == len(events) or attended == k:
                return 0

            start, end, value = events[pos]

            # attend
            next = bisect_left(events, [ end + 1, 0, 0 ])
            best = value   + deeper(next,    attended + 1)
            # or skip
            best = max(best, deeper(pos + 1, attended))
            return best

        return deeper(0, 0)
