class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0

        # position of low and high, not the actual values (which are minK and maxK)
        low  = None
        high = None

        left = 0
        for right, n in enumerate(nums):
            if not (minK <= n <= maxK):
                # requires restart at next position
                left = right + 1
                low  = None
                high = None
                continue

            # note: need to update high/low if we see the same values again
            #       because this will increase the number of valid array
            if n == minK:
                low  = right
            if n == maxK:
                high = right

            if low is not None and high is not None:
                # all arrays between "left" and high/low (whichever came first)
                # are fixed-bound
                result += min(low, high) - left + 1

        return result
