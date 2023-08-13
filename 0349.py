class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)

        result = []
        for a in n1:
            if a in n2:
                result.append(a)
        return result
