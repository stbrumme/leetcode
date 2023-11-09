class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # reservation bitmasks
        rows = defaultdict(int)
        for r, c in reservedSeats:
            rows[r] |= 1 << c

        mask = lambda seats : sum( 1 << s for s in seats )
        middle = mask([ 4,5,6,7 ])
        left   = mask([ 2,3,4,5 ])
        right  = mask([ 6,7,8,9 ])
        both   = left | right

        # capacity if no reservations yet
        result = 2 * n
        for r in rows:
            # bitmask of a row's ten seats
            ten = rows[r]
            if (ten & both) == 0:
                continue # reservations still allow a two groups-of-four

            if (ten & left) == 0 or (ten & right) == 0 or (ten & middle) == 0:
                result -= 1 # only one group-of-four
            else:
                result -= 2 # no group-of-four

        return result
