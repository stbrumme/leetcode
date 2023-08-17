class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse = True)

        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        side = s // 4
        if max(matchsticks) > side:
            return False

        last = min(matchsticks)

        all = [ [ matchsticks[0],0,0,0 ] ]
        del matchsticks[0]
        for stick in matchsticks:
            next = []
            for current in all:
                for pos in range(4):
                    current[pos] += stick
                    gap = side - current[pos]
                    if gap >= 0:
                        s = sorted(current)
                        if (gap == 0 or gap >= last) and s not in next:
                            next.append(s)
                    current[pos] -= stick
            all = next

        return len(all) > 0
