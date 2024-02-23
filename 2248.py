class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
        for row in nums[1 :]:
            result &= set(row)
        return sorted(result)
