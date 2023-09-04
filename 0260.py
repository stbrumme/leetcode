class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        all = 0
        for n in nums:
            all ^= n

        # x^x = 0
        # "all" is result1 ^ result2
        # the lowest set bit in "all" is the first difference between result1 and result2

        # partition all numbers based on that bit
        # there will be two groups with one unique number each
        # repeat the XOR trick to get that number

        mask = 1
        while (all & mask) == 0:
            mask <<= 1

        a = b = 0
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n

        return a, b
