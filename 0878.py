class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # reminds me of FizzBuzz

        # compute n for x
        def count(x):
            # actually the result can be wrong:
            # I don't check whether x is magical
            one  = x // a
            two  = x // b
            both = x // lcm(a, b) # it's possible that a and b share some factors
            return one + two - both

        left  = 0
        right = a * n # rough estimate
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left  = mid + 1
            else:
                right = mid

        return left % 1_000_000_007
