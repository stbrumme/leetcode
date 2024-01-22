class Solution:
    def numWays(self, s: str) -> int:
        mod   = 1_000_000_007

        # count 0s and 1s
        ones  = s.count("1")
        zeros = len(s) - ones

        # only zeros
        if ones == 0:
            # triangle number minus 1
            return ((zeros - 1) * (zeros - 2) // 2) % mod

        if ones % 3 != 0:
            return 0 # no such split
        third = ones // 3

        # number of allowed first and second split position
        split1 = 0
        split2 = 0
        seen = 0 # number of 1s seen so far
        for i, c in enumerate(s):
            if c == "1":
                seen += 1

            if   seen == third:
                split1 += 1
            elif seen == 2 * third:
                split2 += 1
            elif seen > 2 * third:
                break # makes it a tiny bit faster

        return (split1 * split2) % mod
