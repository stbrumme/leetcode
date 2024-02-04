class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # good pair:
        #       j - i = nums[j] - nums[i]
        # nums[i] - i = nums[j] - j
        good = 0
        have = defaultdict(int)
        for i, n in enumerate(nums):
            diff = n - i
            good       += have[diff]
            have[diff] += 1

        size = len(nums)
        all  = size * (size - 1) // 2 # sum(0+1+2+3+4+...+n)
        return all - good
