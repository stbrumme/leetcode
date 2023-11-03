class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # single digit
        both = set(nums1) & set(nums2)
        if both:
            return min(both)

        # two digits
        a = min(nums1)
        b = min(nums2)
        if a < b:
            return a * 10 + b
        else:
            return b * 10 + a
