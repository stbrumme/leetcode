class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        result = set()

        one  = set(nums1)
        two  = set(nums2)
        both = one & two
        need = len(nums1) // 2

        # add as many unique number from first array
        have = 0
        for o in one:
            if have < need and o not in two:
                result.add(o)
                have += 1

        # fill with duplicates
        while have < need and both:
            result.add(both.pop())
            have += 1

        # and second array
        have = 0
        for t in two:
            if have < need and t not in one:
                result.add(t)
                have += 1

        # fill with duplicates
        while have < need and both:
            result.add(both.pop())
            have += 1

        return len(result)
