class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        size = len(batteries)
        batteries.sort()

        # prefix sum
        prefix = [ 0 ]
        for b in batteries:
            prefix.append(prefix[-1] + b)

        def impossible(time):
            need = time * n

            # split batteries
            pos = bisect_left(batteries, time)

            partial = prefix[pos]         # drain the whole battery (maybe in several steps by several computers)
            full    = (size - pos) * time # battery is connected to the same computer all the time
            return partial + full < need

        return bisect_left(range(sum(batteries) + 1), True, key = impossible) - 1
