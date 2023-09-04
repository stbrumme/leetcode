class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # idea: skip one or two houses: never more, never less
        @cache
        def deeper(pos, stop):
            if pos >= stop:
                return 0

            return nums[pos] + max(deeper(pos+2, stop), deeper(pos+3, stop))

        a = deeper(2, len(nums))
        b = deeper(1, len(nums))
        c = deeper(0, len(nums) - 1)
        return max(a, b, c)
