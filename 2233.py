class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()

        # always increment the smallest number by one
        pos = 0
        low = nums[0]
        while k > 0:
            # return to first element
            if pos == len(nums) or nums[pos] >= low:
                pos  = 0
                low += 1

            # increment number and continue with its right neighbor
            k         -= 1
            nums[pos] += 1
            pos       += 1

        # reduce(mul, nums) is too slow because temporary numbers will be huge
        result = 1
        for n in nums:
            result *= n
            result %= 1_000_000_007
        return result
