class Solution:
    def minOperations(self, n: int) -> int:
        result = 0

        limit  = 17 # 2^17 > 10^5
        powers = [ 2**p for p in range(limit + 1) ]

        while n > 0:
            result += 1

            best = +inf
            for p in powers:
                # find closest power of two
                if p >= n:
                    best = min(best, p - n)
                else:
                    best = min(best, n - p)

            n = best

        return result
