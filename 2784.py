class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # remove numbers, must be empty at the end
        need = set(range(1, len(nums)))
        high = 0
        for n in nums:
            need.discard(n)
            if n == len(nums) - 1: # highest number must occur twice
                high += 1

        return high == 2 and not need
