class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # brute-force shows that for n = 0, 1, 2, 3
        # we get 1, 10, 91, 739
        # => OEIS sequence A344389, which is based on A073531
        def A073531(n):
            return 9 * factorial(9) // factorial(10 - n)

        result = 1
        for i in range(1, n+1):
            result += A073531(i)

        return result
