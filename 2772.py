class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        size  = len(nums)
        delta = [ 0 ] * size

        previous = 0
        for i, n in enumerate(nums):
            if i >= k:
                previous -= delta[i - k] # some subarray ends here

            remaining = n - previous
            # a few steps ago we subtracted too much
            if remaining < 0:
                return False

            # we need to subtract beyond the end of the array, which isn't allowed
            if remaining > 0 and i + k > size:
                return False

            delta[i] = remaining # keep track when current subarray ends
            previous = n

        # passed all tests
        return True
