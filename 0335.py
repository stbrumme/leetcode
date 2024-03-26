class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        size = len(distance)
        # three of less lines: impossible to cross itself (remember: distance is guaranteed >= 0)
        if size < 4:
            return False

        # 1. the path must be an ever-growing spiral to avoid self-crossing
        # 2. or it's ever-shrinking
        # whenever it's shrinking and growing at the same time, we have a self-crossing

        c, b, a = distance[ : 3]
        d = e   = -inf
        for i in range(3, size):
            # shift values
            a, b, c, d, e, f = distance[i], a, b, c, d, e

            # shrinking and growing at the same time is a big no-no
            if a >= c and b <= d:
                return True

            # last line is on top of the line a full rotation ago
            if b == d and c <= a + e:
                return True

            # the final case took some time to figure out
            if a >= c - e and b >= d - f and \
               c >= e     and b <= d:
               return True

        return False
