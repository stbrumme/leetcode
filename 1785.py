class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        have = sum(nums)
        need = goal - have
        return ceil(abs(need) / limit)
