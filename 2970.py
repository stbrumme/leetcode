class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                remaining  = nums[:i] + nums[j + 1:]
                increasing = True
                for r in range(1, len(remaining)):
                    increasing &= remaining[r - 1] < remaining[r]
                result += 1 if increasing else 0
        return result
