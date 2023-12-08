class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = 0

        left = 0
        have = set()
        current = 0 # equals sum(have), just a speed trick
        for right in range(len(nums)):
            n = nums[right]
            while n in have:
                have.discard(nums[left])
                current -= nums[left]
                left    += 1

            have.add(n)
            current += n
            result = max(result, current)

        return result
