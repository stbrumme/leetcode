class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            yield nums[i]
            yield nums[i + n]
