class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        size = len(nums)

        # handle edge cases
        if size == 1:
            return -1 if k & 1 else nums[0] # odd => empty pile
        if k <= 1:
            return nums[k]

        # remove k - 1 elements and re-insert their largest
        high = max(nums[ : k - 1])
        # however, if the k-th element is larger, then remove k elements
        if k < size and nums[k] > high:
            return nums[k]

        return high
