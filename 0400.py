class Solution:
    def findNthDigit(self, n: int) -> int:
        # the number has a special name, it's called the Champernowne constant
        # (if joining all digits and preceded them with "0.")

        # I knew it from my Project Euler 40 solution:
        # https://euler.stephan-brumme.com/40/
        # the code below was 1:1 translated from C++ to Python
        # except that variable "pos" is named "n"

        # assume pos has one digit
        digits = 1
        # then there are 9 other numbers
        range  = 9
        # the smallest of them is 1
        first  = 1

        # there are    9 numbers with 1 digits
        # there are   90 numbers with 2 digits
        # there are  900 numbers with 3 digits
        # there are 9000 numbers with 4 digits
        # ...
        # let's figure out the number of digits

        # skip numbers with too few digits
        skip = 0
        while (skip + digits*range < n):
            skip   += digits * range
            # digits = 2 => range = 90 and
            # digits = 3 => range = 900
            # digits = 4 => range = 9000, etc.
            digits += 1
            range  *= 10
            first  *= 10

        # now that we know the number of digits
        # adjust "first" and "skip" such that the left-most/highest digit of pos and skip are identical
        # then continue with the next digit
        while range > 9:
            # could be replace by some modular arithmetic, but I'm too lazy for tough thinking ;-)
            while skip + digits*range < n:
                skip  += digits*range
                first += range

            # next lower digit
            range //= 10 # note: was / in C++, needs to be // in Python (int division)

        # right-most digit (basically same inner loop as above when range == 1)
        while (skip + digits < n):
            first += 1
            skip  += digits

        # skip all "skippable" digits
        n -= skip

        # strings are zero-based whereas input is one-based
        s = str(first)
        return int(s[n - 1])
