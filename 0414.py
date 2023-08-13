class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        all = set(nums)
        if len(all) < 3:
            return max(all)

        all.remove(max(all))
        all.remove(max(all))
        return max(all)
