class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        best = 0
        left = -1
        for right in range(len(nums)):
            if nums[right] == 1:
                best = max(best, right - left)
                continue

            # flip
            if k > 0:
                k -= 1
                best = max(best, right - left)
                continue

            # move to next zero
            left += 1
            while nums[left] == 1:
                left += 1

        return best
