class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        cost   = nums.copy()
        result = sum(nums)

        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                shift = j - i if j >= i else j - i + len(nums)

                if cost[j] > nums[shift]:
                    cost[j] = nums[shift]
                    total  += nums[shift]
                else:
                    total  += cost[j]

            result = min(result, total + i*x) # including cost of rotations

        return result
