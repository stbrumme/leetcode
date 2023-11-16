class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            for j in range(freq):
                yield val
