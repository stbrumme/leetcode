class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # "repeated digits" doesn't mean they have to be next to each other
        # I found it out the hard way ...
        result = 0

        # split into list of digits
        n    = [ int(c) for c in str(n) ]
        size = len(n)

        @cache
        def deeper(need, used, zero, repeated, limit): # used is a bitmask
            if need == 0:
                return 1 if repeated else 0 # 1 if True

            last  = n[-need]
            count = 0
            for digit in range(10):
                # respect upper limit
                if limit and digit > last:
                    break

                # no more leading zeros
                if digit == 1:
                    zero = False

                mask = 1 << digit
                next = used | mask

                if zero:
                    next = 0 # don't count leading zeros

                same = repeated or (used & mask)
                if same:
                    next = 0 # reduce number of memoized states

                count += deeper(need - 1, next, zero, same, limit and digit == last)

            return count

        return deeper(size, 0, True, False, True)
