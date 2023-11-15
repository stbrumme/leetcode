class Solution:
    def isThree(self, n: int) -> bool:
        # 1 and n are always divisors
        if n < 4:
            return False

        # must be square of a prime
        p = int(sqrt(n))
        if n != p * p:
            return False

        # check if p is prime
        if p % 2 == 0:
            return p == 2
        for i in range(3, int(sqrt(p)) + 1, 2):
            if p % i == 0:
                return False

        return True
