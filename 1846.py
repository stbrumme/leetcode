class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        high = 0      # maximum value allowed
        for a in sorted(arr):
            high += 1 # at most 1 higher
            high  = min(a, high)
        return high   # largest value is always at the end
