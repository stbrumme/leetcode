class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # a power-of-two cannot be made from other numbers (except itself)
        # if we have all powers-of-two less than x, then x can be expressed by ORing them
        result = 1

        approach = 3
        # approach 1: 340ms, a set of all numbers
        if approach == 1:
            lookup = set(nums) # faster than scanning a list
            while result in lookup:
                result <<= 1

        # approach 2: 380ms, find powers-of-two with binary search
        elif approach == 2:
            nums.sort()
            while True:
                pos = bisect_left(nums, result)
                if pos == len(nums) or nums[pos] != result:
                    break
                result <<= 1

        # approach 3: 320 ms, extract all powers-of-two
        else:
            have = set()
            for n in nums:
                if (n & (n - 1)) == 0:
                    have.add(n)
            # look for the smallest power-of-two not found:
            while result in have:
                result <<= 1

        return result
