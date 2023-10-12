class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # find largest, remember their original position
        pos = [ (n, i) for i, n in enumerate(nums) ]
        largest = sorted(pos, reverse = True)[:k]
        # restore order
        ordered = sorted([ (i, n) for n, i in largest ])
        return [ n for i, n in ordered ]
