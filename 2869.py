class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        need = set(range(1, k + 1))
        while need:
            need.discard(nums.pop())
            result += 1

        return result
