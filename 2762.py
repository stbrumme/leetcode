class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        have = defaultdict(int)
        left = 0
        for right in range(size):
            # grow sliding window
            have[nums[right]] += 1

            # shrink it
            while max(have) - min(have) > 2:
                drop = nums[left]
                have[drop] -= 1
                if have[drop] == 0:
                    del have[drop]
                left += 1

            result += right - left + 1

        return result
