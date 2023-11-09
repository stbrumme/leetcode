class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # nothing smart, just slicing ...
        result = []
        for i, n in zip(index, nums):
            result = result[:i] + [ n ] + result[i:]
        return result
