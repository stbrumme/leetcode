class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # brute force is easier to code ...
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == diff:
                    for k in range(j + 1, len(nums)):
                        if nums[k] - nums[j] == diff:
                            result += 1
        return result
