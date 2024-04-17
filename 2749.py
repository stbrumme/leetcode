class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for steps in range(60 + 1):
            need = num1 - steps * num2
            if need < 0:
                break # return -1

            # the number of bits must be less or equal to steps
            # "equal": in each step clear one bit with 2^whatever
            # "less":  2^x = 2^(x - 1) + 2^(x - 1)
            #          we can slowly remove bits by choosing smaller exponents for 2^whatever
            #          unfortunately it fails if there are no smaller exponents
            bits = need.bit_count()
            if bits <= steps and steps <= need:
                return steps

        return -1 # failed
