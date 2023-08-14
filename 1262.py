class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)

        if total % 3 == 0:
            return total

        best = 0
        for i in range(len(nums)):
            if (total - nums[i]) % 3 == 0:
                best = total - nums[i]
                break

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                both = nums[i] + nums[j]
                if total - both < best:
                    break
                if (total - both) % 3 == 0:
                    best = total - both
                    break

        return best
