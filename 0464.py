class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def deeper(available): # bitmask
            used = 0
            high = 0
            for i in range(maxChoosableInteger):
                value = i + 1 # zero-based masks
                if available & (1 << i):
                    high  = value
                else:
                    used += value

            if used + high >= desiredTotal:
                return True

            # if opponent can't win, then we win
            for i in range(maxChoosableInteger):
                if available & (1 << i):
                    without = available & ~(1 << i) # clear bit
                    if not deeper(without):
                        return True

            # all paths are forced wins for the opponent
            return False

        # stupid test case with an undefined edge case: not enough numbers for anyone to win
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2 # triangle number
        if total < desiredTotal:
            return False

        return deeper((1 << maxChoosableInteger) - 1)
