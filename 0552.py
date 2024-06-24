class Solution:
    def checkRecord(self, n: int) -> int:
        modulo = 1_000_000_007

        # 6 states:
        # 0 - never absent, never late
        # 1 - never absent, late on previous day
        # 2 - never absent, late on two last days
        # 3 - absent once, never late
        # 4 - absent once, late on previous day
        # 5 - absent once, late on two last days
        good = [ 1, 0, 0, 0, 0, 0 ]
        for i in range(n):
            good = [ sum(good[ : 3]), good[0], good[1], sum(good), good[3], good[4] ]

            # a little bit faster if delaying modulo
            if (i & 31) == 31: # temporary numbers still fit in 64 bit
                for j in range(6):
                    good[j] %= modulo

        return sum(good) % modulo
