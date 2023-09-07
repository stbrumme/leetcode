class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # integer
        if numerator % denominator == 0:
            return str(numerator // denominator)

        negative = (numerator * denominator < 0)
        numerator   = abs(numerator)
        denominator = abs(denominator)

        # integer part
        prefix = str(numerator // denominator) + "."
        numerator %= denominator
        if negative:
            prefix = "-" + prefix

        remainders = { }
        digits = 0
        suffix = ""
        while True:
            # remainder seen before ?
            if numerator in remainders:
                begin  = remainders[numerator]
                repeat = suffix[begin:]
                if repeat == "0":
                    return prefix + suffix[:begin]

                suffix = suffix[:begin] + "(" + suffix[begin:] + ")"
                return prefix + suffix

            remainders[numerator] = digits

            # chop off
            numerator *= 10
            next       = str(numerator // denominator)
            numerator %= denominator

            suffix += next
            digits += 1
