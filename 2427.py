class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        result = 0

        shared = gcd(a, b)
        for factor in range(1, shared + 1):
            if shared % factor == 0:
                result += 1

        return result
