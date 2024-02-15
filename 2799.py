class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        result   = 0
        size     = len(nums)
        distinct = len(set(nums))

        # brute force
        for i in range(size):
            have = set()
            for j in range(i, size):
                have.add(nums[j])
                if len(have) == distinct:
                    result += 1

        return result
