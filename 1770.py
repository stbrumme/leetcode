class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def deeper(left, right): # numbers already removed on the left and right side of nums
            m = left + right
            if m == len(multipliers):
                return 0

            a = multipliers[m] * nums[left]         + deeper(left + 1, right)
            b = multipliers[m] * nums[-(right + 1)] + deeper(left, right + 1)
            return max(a, b)

        return deeper(0, 0)
