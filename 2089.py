class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [ i for i, n in enumerate(sorted(nums)) if n == target ]
