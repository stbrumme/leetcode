class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in set(nums1):
            freq[n] += 1
        for n in set(nums2):
            freq[n] += 1
        for n in set(nums3):
            freq[n] += 1

        for f in freq:
            if freq[f] >= 2:
                yield f
