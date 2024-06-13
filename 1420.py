class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        modulo = 1_000_000_007

        @cache
        def deeper(pos, high, cost):
            if pos == n:
                return 1 if cost == k else 0

            # append a smaller number (choose any number from [ 1, high ])
            result = high *   deeper(pos + 1, high, cost)
            # append a new maximum
            if cost < k:
                for i in range(high + 1, m + 1):
                    result += deeper(pos + 1, i,    cost + 1)

            return result % modulo

        return deeper(0, 0, 0)
