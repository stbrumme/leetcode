class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = set(nums1)
        two = set(nums2)
        yield sum(1 for n in nums1 if n in two)
        yield sum(1 for n in nums2 if n in one)
