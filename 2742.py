class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        result  = 0

        # longest jobs first, triggers early exit in the main loops more frequently
        jobs = sorted(list(zip(time, cost)), reverse = True)
        size = len(jobs)

        @cache
        def deeper(pos, freetime): # "freetime" denotes the time units where the paid painter is still working
                                   # and the free painter can finish some walls
            if pos == size:
                return 0 if freetime >= 0 else +inf # abort, no solution

            # early exit: paint all walls with free painter because the paid one was very busy
            remaining = size - pos
            if remaining <= freetime:
                return 0

            hours, dollars = jobs[pos]

            one = dollars + deeper(pos + 1, freetime + hours)
            two =           deeper(pos + 1, freetime - 1)
            # choose cheaper path
            return min(one, two)

        return deeper(0, 0)
