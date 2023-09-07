class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b < a:
                break

            other = bisect_right(nums, b)
            between = other - i - 1
            # each number between a and b can be there or not => like bits in a binary numbers
            result += 2**between

            result %= 10**9 + 7

        return result
