class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0

        # a short solution would iterate over all indices and look at bit_count
        # but let's try some tricks with permutations and generate only relevant indices

        # maximum number of bits
        bits = len(bin(len(nums))) - 2 # skip "0b"
        # [ 0,0,0,...,0,1,1,...,1 ]
        base = [ 0 ] * (bits - k) + [ 1 ] * k

        # unfortunately, there is no parameter for itertools to enforce skipping repeated items
        # therefore a set() must eliminate duplicates
        for x in set(permutations(base)):
            index = sum(value << i for i, value in enumerate(x))
            # a few permutations might be out of range
            if index < len(nums):
                result += nums[index]

        # actually, the short solution would be faster ...
        return result
