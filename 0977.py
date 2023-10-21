class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([ n*n for n in nums ])
