class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        have = {}
        for n in sorted(nums):
            have[n + 1] = have.get(n,     0) + 1
            have[n    ] = have.get(n - 1, 0) + 1

        return max(have.values())
