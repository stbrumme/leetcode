class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = +inf

        nums.sort()
        for i in range(k - 1, len(nums)):
            one = nums[i - k + 1]
            two = nums[i]
            result = min(result, two - one)

        return result
