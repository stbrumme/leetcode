class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        low  = [ 0 ] * size # minimum of nums[k : ]
        have = +inf
        for i in reversed(range(size)):
            have = min(have, nums[i])
            low[i] = have

        high = nums[0]
        for i in range(1, size - 1):
            n = nums[i]
            if   high        < n < low [i + 1]:
                result += 2
            elif nums[i - 1] < n < nums[i + 1]:
                result += 1

            high = max(high, n)

        return result
