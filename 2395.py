class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        have = set()
        for a, b in zip(nums, nums[1:]):
            if a + b in have:
                return True
            have.add(a + b)

        return False
