class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        for denominator in range(1, n + 1):
            for numerator in range(1, denominator):
                if gcd(denominator, numerator) == 1:
                    yield str(numerator) + "/" + str(denominator)
