class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reverse order: find last balloon between left and right (NOT inclusive)
        @cache
        def deeper(left, right):
            if left == right:
                return nums[left]

            last = 0
            # skip borders, find last balloon between them
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                last = max(last, deeper(left, i) + coins + deeper(i, right))
            return last
        
        # add boundaries to avoid edge cases
        nums = [ 1 ] + nums + [ 1 ]
        return deeper(0, len(nums) - 1)