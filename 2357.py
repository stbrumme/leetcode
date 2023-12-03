class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set(nums)
        unique.discard(0)
        return len(unique)
