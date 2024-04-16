class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        result = 1

        have = defaultdict(list)
        for i, n in enumerate(nums):
            have[n].append(i)
            while have[n][0] <= i - (len(have[n]) + k):
                have[n].pop(0)

            result = max(result, len(have[n]))

        return result
