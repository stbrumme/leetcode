class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = defaultdict(int)
        for a in nums1:
            freq[a] += 1

        result = []
        for a in nums2:
            if a in freq and freq[a] > 0:
                result.append(a)
                freq[a] -= 1
        return result
