class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        result = +inf
        size   = len(nums)

        for start in [ 0, 1 ]:
            steps = 0
            # decrement every second value until it's lower than its neighbors
            for i in range(start, size, 2):
                low = nums[i]

                # must be lower than left  side
                if i > 0:
                    low = min(low, nums[i - 1] - 1)
                # must be lower than right side
                if i < size - 1:
                    low = min(low, nums[i + 1] - 1)

                steps += nums[i] - low

            result = min(result, steps)

        return result
