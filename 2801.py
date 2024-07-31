class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        @cache
        def deeper(pos, previous, limit): # previous = -1 means "no digit" (= leading zero)
            nonlocal size
            if pos == size:
                return previous >= 0 # 1 if valid number, 0 if previous is still -1

            # highest digit for current position
            last = digits[pos] if limit else 9

            result = 0
            if previous == -1:
                # leading zero
                result = deeper(pos + 1, -1, False)
                # start number
                for i in range(1, last + 1): # don't start with zero
                    result += deeper(pos + 1, i,    limit and i    == last)
            else:
                # what goes up ...
                up   = previous + 1
                if up <= last:
                    result += deeper(pos + 1, up,   limit and up   == last)

                # ... must come down
                down = previous - 1
                if 0 <= down <= last:
                    result += deeper(pos + 1, down, limit and down == last)

            return result

        # step 1: compute [ 1 ... high ]
        size   = len(high)
        digits = [ int(c) for c in high ]
        one    = deeper(0, -1, True)

        # step 2: compute [ 1 ... low - 1 ]
        low    = str(int(low) - 1) # Python supports large integers
        size   = len(low)
        digits = [ int(c) for c in low ]
        deeper.cache_clear()       # important ! avoid collision with step 1
        two    = deeper(0, -1, True)

        return (one - two) % 1_000_000_007
