class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1

        next = primes.copy() # sorted => can be used as a min-heap instantly

        while n > 2:
            current = heappop(next)
            # repeated same number
            while next and next[0] == current:
                heappop(next)

            for p in primes:
                heappush(next, current * p)

            n -= 1

        return heappop(next)
