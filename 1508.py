class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # count all sums
        size = len(nums)
        all  = []
        for i in range(size):
            total = 0
            for j in range(i, size):
                total += nums[j]
                all.append(total)

        all.sort()

        return sum(all[left - 1 : right]) % 1_000_000_007
