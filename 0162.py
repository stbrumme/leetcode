class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # just for fun: a randomized approach
        size = len(nums)
        if size <= 1:
            return 0

        while True:
            pos = randint(0, size - 1)
            left = right = -2**32
            if pos > 0:
                left  = nums[pos - 1]
            if pos < size - 1:
                right = nums[pos + 1]
            if left < nums[pos] and nums[pos] > right:
                return pos

        return 0
