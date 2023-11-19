class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        result = 0

        # diffs between consecutive (sorted) numbers
        nums.sort()
        diffs = []
        for i in range(1, len(nums)):
            diffs.append(nums[i] - nums[i - 1])

        have  = 0
        total = 0
        left  = 0
        for right in range(len(diffs)):
            # add differences
            width  = right - left + 1
            have  += diffs[right] * width
            total += diffs[right]

            # shrink sliding window if too much
            while have > k:
                width -= 1
                have  -= total
                total -= diffs[left]
                left  += 1

            result = max(result, width)

        return result + 1 # diff is always between two numbers, therefore +1
