class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        max1 = nums[len(nums) - 1]
        max2 = nums[len(nums) - 2]

        limit = 10**5
        high = +limit
        low  = -limit

        for i in range(len(nums)):
            # optimization
            if nums[i] + max2 + max1 <= low:
                continue

            for j in range(i+1, len(nums)):
                # optimization
                if nums[i] + nums[j] + max1 <= low:
                    continue

                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if high > sum and sum >= target:
                        high = sum
                    if low  < sum and sum <= target:
                        low = sum

                    # optimization
                    if sum >= target:
                        break

        diffHigh = abs(high - target)
        diffLow  = abs(low  - target)
        if diffHigh < diffLow:
            return high
        else:
            return low
