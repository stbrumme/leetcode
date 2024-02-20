class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        all = { id: value for id, value in nums1 }
        for id, value in nums2:
            all[id] = all.get(id, 0) + value
        return sorted( all.items() )
