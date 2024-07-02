class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)

        # "*"
        star = ( 1,2,3,4,5,6,7,8,9 )

        # our own caching, faster than @cache
        cache = [ [ None ] * size for _ in range(10)]

        def deeper(previous, pos):
            if pos == size:
                # must not have a pending digit
                return 0 if previous else 1

            if cache[previous][pos] != None:
                return cache[previous][pos]

            total = 0
            candidates = star if s[pos] == "*" else ( int(s[pos]), )
            for c in candidates:
                if previous > 0:
                    both = previous * 10 + c
                    if 10 <= both <= 26:
                        total += deeper(0, pos + 1)
                else:
                    if   1 <= c <= 2:
                        total += deeper(0, pos + 1) + deeper(c, pos + 1)
                    elif 3 <= c:
                        total += deeper(0, pos + 1)

            total %= 1_000_000_007
            cache[previous][pos] = total
            return total

        return deeper(0, 0)
