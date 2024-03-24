class Solution:
    def stringCount(self, n: int) -> int:
        # bitmask: lowest 4 bits represent LEET
        L   = 1 << 3 # 8
        E1  = 1 << 2 # 4
        E2  = 1 << 1 # 2
        T   = 1 << 0 # 1
        all = L | E1 | E2 | T # 15

        modulo = 1_000_000_007

        @cache
        def deeper(i = 0, bitmask = 0):
            if i == n:
                return bitmask // all # my extra weird way to say "return 1 if bitmask == 15 else 0"

            # append neither l, e nor t
            other = deeper(i + 1, bitmask) * (26 - 3)

            # append l or t
            l     = deeper(i + 1, bitmask | L)
            t     = deeper(i + 1, bitmask | T)

            # append e (slightly trickier than l or t, because we need it twice)
            if bitmask & E1:
                bitmask |= E2
            else:
                bitmask |= E1
            e     = deeper(i + 1, bitmask)

            return (other + l + e + t) % modulo

        return deeper()
