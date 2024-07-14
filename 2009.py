class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = +inf

        size   = len(nums)
        unique = sorted(set(nums))

        for left, n in enumerate(unique):
            # sequence n, n+1, n+2, ..., n + size - 1
            right  = bisect_right(unique, n + size - 1)
            length = right - left + 1
            result = min(result, size - length + 1)

        return result
