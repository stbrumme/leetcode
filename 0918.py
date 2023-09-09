class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        high = 0
        low  = 0
        positive = float("-inf")
        negative = float("+inf")

        # twice Kadane
        total = 0
        for n in nums:
            total   += n

            # maximum
            high    += n
            positive = max(positive, high)
            high     = max(0, high)

            # minimum
            low     += n
            negative = min(negative, low)
            low      = min(0, low)

        if total - negative == 0:
            return positive
        return max(positive, total - negative)
