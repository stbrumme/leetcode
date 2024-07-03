class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = -inf

        total  = 0
        have   = {}
        for i, n in enumerate(nums):
            # maximize prefix sum for current value
            if n not in have or total - have[n] < 0:
                have[n] = total

            # update prefix sum
            total += n

            # absolute value means two choices: n - k and n + k
            if n - k in have:
                result = max(result, total - have[n - k])
            if n + k in have:
                result = max(result, total - have[n + k])

        return result if result != -inf else 0
