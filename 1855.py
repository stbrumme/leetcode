class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        i = 0
        for j in range(len(nums2)):
            while i < len(nums1) - 1 and i < j and nums1[i] > nums2[j]:
                i += 1

            if nums1[i] <= nums2[j]:
                distance = j - i
                result   = max(result, distance)

        return result
