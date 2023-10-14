class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # multiples of 2 and/or 5 never end with "1"
        if k % 2 == 0 or k % 5 == 0:
            return -1

        # https://oeis.org/A067063

        # repunit(k - 1) or repunit(k) is always a multiple of k if such a relation exists
        # maybe there is a smaller solution but definitely never a need to look beyond k

        # honestly this problem stinks because it's very simple programming
        # but you need a math knowledge not taught outside university math courses

        # on top, I have no idea how to solve this in C/C++ where numbers must fit in 64 bit
        ones = 1
        for i in range(1, k + 1):
            if ones % k == 0:
                return i

            ones *= 10
            ones +=  1

        return -1
