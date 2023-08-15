class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask = 1
        while mask < max(left, right):
            mask <<= 1

        while (left & mask) == (right & mask) and mask > 0:
            mask >>= 1

        while mask > 0:
            left &= ~mask
            mask >>= 1

        return left
