class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # this is a pure math problem
        # don't know why it's on Leetcode ...

        # select two numbers a and b
        # we need to find x and y such that ax + by = 1
        # this is only possible if they share no prime factor
        return gcd(*nums) == 1
