class Solution:
    def integerBreak(self, n: int) -> int:
        best = 0
        for k in range(2, n+1):
            x = n // k
            remainder = n % k

            product = 1
            for i in range(k):
                if remainder > 0:
                    product *= x + 1
                    remainder -= 1
                else:
                    product *= x

            best = max(best, product)

        return best
