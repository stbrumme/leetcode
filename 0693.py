class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= n >> 1 # now all bits set
        n += 1      # now power of two
        return (n & (n - 1)) == 0 # clear lowest bit
