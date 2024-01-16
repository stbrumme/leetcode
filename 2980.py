class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # look for at least two even numbers
        return reduce(lambda a, b: a + ((b & 1) ^ 1), [ 0 ] + nums) > 1
