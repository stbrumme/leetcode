class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def deeper(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            one  = deeper(i + 1, j)
            two  = deeper(i, j + 1)
            both = max(0, nums1[i] * nums2[j]) + deeper(i + 1, j + 1) # both or none (<= if one is negative)
            return max(one, two, both)

        result = deeper(0, 0)
        # special case: non-positive numbers in one array
        if result == 0:
            if max(nums1) <= 0:
                return max(nums1) * min(nums2)
            else:
                return min(nums1) * max(nums2)

        return result
