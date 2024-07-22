class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def deeper(left, right):
            if right - left < 1:
                return 0

            best = 0
            if nums[left]  + nums[left + 1]  == both:
                best =           1 + deeper(left + 2, right)
            if nums[right] + nums[right - 1] == both:
                best = max(best, 1 + deeper(left,     right - 2))
            if nums[left]  + nums[right]     == both:
                best = max(best, 1 + deeper(left + 1, right - 1))

            return best

        size   = len(nums)

        both   = nums[0] + nums[1]
        result = deeper(0, size - 1)

        if both != nums[-1] + nums[-2]:
            deeper.cache_clear()
            both   = nums[-1] + nums[-2]
            result = max(result, deeper(0, size - 1))

        if both != nums[0] + nums[-1]:
            deeper.cache_clear()
            both   = nums[0] + nums[-1]
            result = max(result, deeper(0, size - 1))

        return result
