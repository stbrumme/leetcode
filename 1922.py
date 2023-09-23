class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd  = n // 2
        even = n - odd
        mod  = 10**9 + 7
        return (pow(4, odd, mod) * pow(5, even, mod)) % mod