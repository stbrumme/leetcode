class Solution:
    def canWinNim(self, n: int) -> bool:
        # 1. if less than four stones are left, you win
        # 2. if four stones are left, you lose
        # 3. step 2 is impossible if n is a multiple of 4 and your opponent takes 4-x stones after you took x stones
        return n % 4 != 0
