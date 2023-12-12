class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        both = set(nums1) & set(nums2)
        return min(both) if both else -1
