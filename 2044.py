class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result = 0
        size = len(nums)

        # ORing all numbers gives us the "maximum bitwise OR"
        high = 0
        for n in nums:
            high |= n

        # process all subsets
        for i in range(2**size):
            have = 0
            for j in range(size):
                if i & (1 << j):
                    have |= nums[j]
            if have == high:
                result += 1

        return result
