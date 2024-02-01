class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return [ (n & 0b0101010101).bit_count(), (n & 0b1010101010).bit_count() ]
