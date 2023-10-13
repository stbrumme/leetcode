class Solution:
    def baseNeg2(self, n: int) -> str:
        # based on https://oeis.org/A039724
        s = ""
        while n >= 2 or n < 0:
            # integer division, keep remainder
            r = n %  -2
            n = n // -2
            # make sure that remainder is always positive
            if r < 0:
                r += 2
                n += 1

            s = str(r) + s

        return str(n) + s
