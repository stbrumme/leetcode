class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        pos = {}
        for i in range(len(nums2)):
            pos[nums2[i]] = i

        for i in nums1:
            j = pos[i] + 1

            while j < len(nums2) and nums2[j] < i:
                j += 1

            if j == len(nums2):
                result.append(-1)
            else:
                result.append(nums2[j])

        return result
