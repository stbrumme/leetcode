class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        for i in range(21): # 3^21 > 2^32
            triple = 3**i
            if triple == n:
                return True
            if triple > n:
                break

        return False
