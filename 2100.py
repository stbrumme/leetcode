class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        size = len(security)
        if time == 0:
            # why does that fail: return list(range(size))
            for i in range(size):
                yield i
            return

        # count days with increasing guards
        increase = [ 0 ] * size
        for i in reversed(range(size - 1)):
            if security[i] <= security[i + 1]:
                increase[i] = increase[i + 1] + 1

        # decreasing number of guards
        decrease = 0
        for i in range(1, size):
            if security[i] <= security[i - 1]:
                # one more
                decrease += 1
                if min(decrease, increase[i]) >= time:
                    yield i
            else:
                # restart
                decrease = 0
