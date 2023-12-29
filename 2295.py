class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        have = { n: i for i, n in enumerate(nums) }
        for a, b in operations:
            pos = have[a]
            del have[a]
            have[b]   = pos
            nums[pos] = b

        return nums
