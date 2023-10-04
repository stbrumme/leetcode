class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        data = sorted([ (n, i) for i, n in enumerate(nums) ], reverse = True)
        return data[0][1] if data[0][0] >= 2 * data[1][0] else -1
