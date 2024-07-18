class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # three cases:
        # 1) n % 3 == 0, do nothing
        # 2) n % 3 == 1, subtract 1
        # 3) n % 3 == 2, add 1
        return sum(n % 3 != 0 for n in nums)
