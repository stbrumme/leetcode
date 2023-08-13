class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(16): # 4^16 > 2^31
            if 4**i == n:
                return True
        return False
