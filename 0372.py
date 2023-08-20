class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # nothing's forbidden, therefore Python should do the hard work ;-)
        exponent = 0
        for x in b:
            exponent *= 10
            exponent += x

        return pow(a, exponent, 1337) # it's powmod
