class Solution:
    def nthUglyNumber(self, n: int) -> int:
        next = [ 1 ]

        for _ in range(n - 1):
            current = heappop(next)
            while next and next[0] == current:
                heappop(next)

            heappush(next, current * 2)
            heappush(next, current * 3)
            heappush(next, current * 5)

        return next[0]
