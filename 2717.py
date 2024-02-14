class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums.index(1)
        last  = nums.index(n)

        result = first + (n - last - 1)
        if first > last:
            result -= 1 # one shared swap

        return result
