class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        have = set(nums)
        for n in nums:
            have.add(int(str(n)[::-1]))
        return len(have)
