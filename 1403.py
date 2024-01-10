class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort()

        have = 0
        while have <= total // 2:
            have += nums[-1]
            yield nums.pop()
