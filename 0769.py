class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        high   = -1
        for pos, n in enumerate(arr):
            if high < n:
                high = n
            if pos == high:
                result += 1
                high = -1

        return result