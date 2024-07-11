class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = str(n)
        size   = len(digits)

        @cache
        def deeper(pos, have, limited):
            if pos == size:
                return 1

            # simplify last digit
            if pos == size - 1 and not limited:
                return 10 - have.bit_count()

            # don't exceed n
            high = 10
            if limited:
                high = int(digits[pos])

            result = 0
            for i in range(10):
                mask = 1 << i

                # only if new digit
                if not (have & mask):
                    if i == 0 and have == 0: # leading zeros don't affect whether a number is special
                                             # (but are important to process short numbers)
                        result += deeper(pos + 1, have       , i == high)
                    else:
                        result += deeper(pos + 1, have | mask, i == high)

                # respect upper limit
                if i == high:
                    break

            return result

        return deeper(0, 0, True) - 1 # lowest valid number is 1, not 0
