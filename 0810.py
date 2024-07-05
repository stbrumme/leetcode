class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # the last player who removes a number always loses
        if (len(nums) & 1) == 0:
            return True

        # odd count
        return reduce(xor, nums) == 0
