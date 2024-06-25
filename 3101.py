class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        result = 1
        length = 1
        for a, b in zip(nums, nums[1 : ]):
            length  = 1 if a == b else length + 1
            result += length

        return result
