class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # range of potential divisors
        left  = 1
        right = max(nums)

        # binary search
        while left != right:
            # mid => divisor
            mid = (left + right) // 2

            # note: problem asks for rounding up
            total = sum(int(ceil(n / mid)) for n in nums)
            if total > threshold:
                left  = mid + 1
            else:
                right = mid

        return left # == right
