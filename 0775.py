class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # count local inversions
        loc = 0
        for a, b in zip(nums, nums[1 :]):
            loc += a > b

        # count global inversions
        glo  = 0
        seen = []
        for n in nums:
            bigger = bisect_left(seen, n)
            glo   += len(seen) - bigger
            if glo > loc:
                break

            insort(seen, n) # happens most likely at the end, which should be quite fast

        return loc == glo
