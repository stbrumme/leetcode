class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        # no swap needed
        if ones <= 1:
            return 0

        # initial segment
        have = nums[ : ones].count(1)
        best = ones - have
        # duplicate data to simulate wraparound
        twice = nums + nums[ : ones]
        # sliding window
        for right in range(ones, len(twice)):
            have += twice[right]
            have -= twice[right - ones]
            best  = min(best, ones - have)
            # early exit
            if best == 0:
                break
        return best
