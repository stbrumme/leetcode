class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0

        prefix = defaultdict(int)
        prefix[0] = 1

        total = 0
        for n in nums:
            total  += n
            result += prefix[total - goal]
            prefix[total] += 1

        return result
