class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        @cache
        def deeper(one, two, delta, skipped):
            if skipped == 3:
                return False # remove at most 2
            if two == len(nums2):
                return True  # nums2 completely mapped, remove all remaining in nums1

            if nums2[two] - nums1[one] == delta:
                # match
                return deeper(one + 1, two + 1, delta, skipped)
            else:
                return deeper(one + 1, two,     delta, skipped + 1)

        result = []
        for i in range(3):
            diff = nums2[0] - nums1[i]
            if deeper(i, 0, diff, i):
                result.append(diff)

        return min(result)
