class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        # find largest range [ n, n * k ]
        return max(bisect_right(nums, n + 2 * k, lo = i) - i for i, n in enumerate(nums) )
