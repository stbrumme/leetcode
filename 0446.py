class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        seqs = defaultdict(int)

        for i in range(size):
            for j in range(i):
                diff = nums[i] - nums[j]
                have = seqs[(j, diff)]
                seqs[(i, diff)] += have + 1 # extend sequence by one element

                result += have              # can be zero => less than three elements

        return result
