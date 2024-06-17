class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        all = [ ( e, s ) for e, s in zip(efficiency, speed ) ]
        all.sort(reverse = True)

        result = 0
        total  = 0 # sum(speed of selected engineers)

        # pick most efficient first, keep track of the slowest
        team = []
        for e, s in all:
            # add an engineer to the team
            total += s
            heappush(team, s)

            # maximum team size reached. drop the slowest
            if len(team) > k:
                total -= heappop(team)

            # current engineer is the least efficient
            result = max(result, total * e)

        return result % 1_000_000_007
