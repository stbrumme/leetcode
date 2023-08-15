class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = sum(nums)
        digit = 0
        for i in nums:
            while i > 0:
                digit += i % 10
                i //= 10

        return element - digit
