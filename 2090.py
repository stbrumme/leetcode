class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        size   = len(nums)
        length = 2 * k + 1 # how many numbers are part of a k-radius

        total  = 0 if length > size else sum(nums[ : length - 1])
        for i in range(size):
            left  = i - k
            right = i + k
            if left < 0 or right >= size:
                # outside
                yield -1
            else:
                # valid average
                total += nums[right]
                yield total // length
                total -= nums[left]
