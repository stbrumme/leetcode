class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (k ^ reduce(xor, nums)).bit_count()
