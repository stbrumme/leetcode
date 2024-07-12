class Solution:
    def distinctSequences(self, n: int) -> int:
        # precomputed table gcd(i, good[i]) == 1 and i != good[i]
        good = ( ( 1, 2, 3, 4, 5, 6 ),  # zero is only valid for seeding "one"
                 (    2, 3, 4, 5, 6 ),  # 1
                 ( 1,    3,    5    ),  # 2
                 ( 1, 2,    4, 5    ),  # 3
                 ( 1,    3,    5    ),  # 4
                 ( 1, 2, 3, 4,    6 ),  # 5
                 ( 1,          5    ) ) # 6

        @lru_cache(maxsize = 50_000)
        def deeper(pos, one, two): # one & two refer to the last two rolls
            return 1 if pos == n else sum(deeper(pos + 1, dice, one) for dice in good[one] if dice != two ) % 1_000_000_007

        return deeper(0, 0, 0)
