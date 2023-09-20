class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1

        # greedy left side
        left = a = 0
        while a < x:
            a    += nums[left]
            left += 1

        best = left if a == x else float("inf")

        # right side
        right = b = 0
        while right < len(nums):
            right += 1
            b     += nums[-right]

            # fix overshooting
            while a + b > x and left > 0:
                left -= 1
                a    -= nums[left]

            if a + b == x:
                best = min(best, left + right)

        return best if best < float("inf") else -1