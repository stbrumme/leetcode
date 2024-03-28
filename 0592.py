class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = [] # numerators
        d = [] # denominators

        sign    = +1 # if no sign then plus
        value   =  0 # current number, parse digit by digit

        # extract all numbers, incl. sign
        for c in expression + "+": # add dummy char to fetch the last number without hassle
            if c in "0123456789":  # another digit
                value *= 10
                value += int(c)
            else:
                # not a digit, therefore store the
                if value > 0: # value is only zero if input starts with "-"
                    # split into numerator and denominator
                    value *= sign
                    if len(n) == len(d):
                        n.append(value)
                    else:
                        d.append(value)
                    # reset
                    value = 0
                    sign  = +1

                # could by a sign
                if   c == "+":
                    sign  = +1
                elif c == "-":
                    sign  = -1
                # or "/", nothing to do in that case

        # product of all denominators
        full_d = reduce(mul, d)
        # convert each numerator such that it belongs to that "unified" denominator
        full_n = 0
        for nn, dd in zip(n, d):
            full_n += nn * full_d // dd

        # edge case
        if full_n == 0:
            return "0/1"

        # make it irreducible, divide by greatest common divisor
        shared = gcd(full_n, full_d)
        full_n //= shared
        full_d //= shared
        return f"{full_n}/{full_d}"
