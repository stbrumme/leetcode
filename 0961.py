class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        have = set()
        for n in nums:
            if n in have:
                return n # don't check if it's n+1 times
                         # just return the first number that occurs multiple times
            have.add(n)
