class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum  = 0
        result = float("inf")
        for right in range(len(nums)):
            # grow
            sum += nums[right]

            # shrink
            while sum - nums[left] >= target:
                sum  -= nums[left]
                left += 1

            if sum >= target:
                result = min(result, right - left + 1)

        return result if result < float("inf") else 0
