class Solution:
    @cache
    def deeper(self, a, b):
        emptyA = a <= 0
        emptyB = b <= 0
        if emptyA and emptyB:
            return 0.5
        if emptyA:
            return 1
        if emptyB:
            return 0

        m = self.deeper(a - 4, b)
        n = self.deeper(a - 3, b - 1)
        o = self.deeper(a - 2, b - 2)
        p = self.deeper(a - 1, b - 3)
        return (m + n + o + p) / 4

    def soupServings(self, n: int) -> float:
        # result converges to 1
        if n > 4900:
            return 1

        # reduce state space, round up
        simpler = (n + 24) // 25
        return self.deeper(simpler, simpler)
