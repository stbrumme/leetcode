class Solution:
    def smallestValue(self, n: int) -> int:
        while n not in [ 0, 1, 2, 3, 4, 5, 7 ]: # 0,1,4 => loop, all others are primes
            sum = 0
            old = n

            # even
            while n % 2 == 0:
                n //= 2
                sum += 2

            # odd
            factor = 3
            step = 2
            while factor*factor <= n:
                # simplified wheel-6
                while n % factor == 0:
                    n //= factor
                    sum += factor
                factor += step
                if factor >= 7:
                    step = 4 - step

            if n == old:
                break

            # last prime factor
            if n > 1:
                sum += n

            n = sum

        return n
