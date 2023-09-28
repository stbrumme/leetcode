class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        #    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # => nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        diffs = defaultdict(int)
        result = 0
        for n in nums:
            r = int(str(n)[::-1]) # Python ignores leading zeros
            d = n - r
            result   += diffs[d]
            diffs[d] += 1

        return result % (10**9 + 7)
