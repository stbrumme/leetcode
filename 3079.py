class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(len(str(n)) * max(str(n))) for n in nums)
