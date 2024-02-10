class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0

        prev = +inf
        for i, n in enumerate(nums):
            left  = 0 # delta of left neighbor
            for j in reversed(range(i)):
                if nums[i] != nums[j]:
                    left = nums[i] - nums[j]
                    break

            right = 0 # delta of right neighbor
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    right = nums[i] - nums[j]
                    break

            if left * right > 0 and n != prev: # both positive or negative
                result += 1
            prev = n

        return result
