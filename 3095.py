class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result = +inf

        # brute force
        size = len(nums)
        for i in range(size):
            have = 0
            for j in range(i, size):
                have |= nums[j]
                if have >= k:
                    result = min(result, j - i + 1)
                    break

        return result if result != +inf else -1
