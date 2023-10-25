class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)
        diff = a - b # may be negative

        hashed = set(bobSizes)
        for i in aliceSizes:
            j = i - diff / 2
            if j in hashed:
                return [ i, j ]
