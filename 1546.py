class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        result = 0

        have  = set([ 0 ])
        total = 0
        for n in nums:
            # prefix sum
            total += n

            if total - target in have:
                result += 1
                have.clear()

            have.add(total)

        return result
