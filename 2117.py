class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        # use Python's large integers (multiplying 1 thru 10^4 creates about 35000 digits)
        sys.set_int_max_str_digits(0) # default was 4300

        # slower version
        #all = reduce(lambda a, b : a * b, range(left, right + 1))

        # slightly faster: process groups of 10 to avoid too many large-number multiplications
        all  = 1
        tens = 0
        step = 10
        for i in range(left, right + 1, step):
            partial = reduce(lambda a, b : a * b, range(i, min(right + 1, i + step)))

            a, b = divmod(partial, 10)
            while b == 0:
                partial = a
                tens   += 1
                a, b    = divmod(partial, 10)

            all *= partial

        a = str(all)
        # strip zeros
        digits = a.rstrip("0")
        tens  += len(a) - len(digits)

        # replace by short notation
        if len(digits) > 10:
            digits = digits[ : 5] + "..." + digits[-5 : ]
        return digits + "e" + str(tens)
