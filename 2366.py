class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result = 0

        # there's no way to increase a number
        # therefore the last number of each subarray must be its largest
        # we must number in front of it to make the subarray non-decreasing

        high = nums[-1]
        while nums:
            last = nums.pop()
            if high >= last:
                # already non-decreasing
                high = last
            else:
                # split evenly
                steps = (last - 1) // high
                high  = last // (steps + 1)

                result += steps

        return result
