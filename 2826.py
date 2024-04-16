class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        size = len(nums)

        @cache
        def deeper(pos, low = 1):
            if pos == size:
                return 0

            value = nums[pos]

            # do nothing
            keep =     deeper(pos + 1, value)
            # remove element
            take = 1 + deeper(pos + 1, low)

            if value < low:
                return take            # no choice, must remove
            if value > low:
                return min(keep, take) # both options are possible

            # nums[pos] == low
            return keep

        return deeper(0)
