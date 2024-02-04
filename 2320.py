class Solution:
    def countHousePlacements(self, n: int) -> int:
        # https://oeis.org/A007598
        # squared Fibonacci numbers, shifted by 2
        @cache
        def fib(x):
            return x if x <= 1 else fib(x - 2) + fib(x - 1)

        return pow(fib(n + 2), 2, 1_000_000_007)
