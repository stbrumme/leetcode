class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        need = 0 # values of the current "bit block" need to be higher than this
        high = 0 # highest value in current bit block
        bits = 0 # set bits in current bit block
        for n in nums:
            # new block
            if n.bit_count() != bits:
                bits = n.bit_count()
                need = high

            # check if sorted with regards to previous block
            if n < need:
                return False
            high = max(high, n)

        return True
