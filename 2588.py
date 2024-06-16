class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # the problem description in one sentence:
        # count all subarrays where XORing all their values yield zero
        result = 0

        total = 0
        have  = defaultdict(int)
        for n in [ 0 ] + nums:
            total  ^= n
            result += have[total]
            have[total] += 1

        return result
