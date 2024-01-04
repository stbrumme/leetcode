class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        result = 1
        nums.sort() # actually the order of nums doesn't matter
        low = nums[0]
        for n in nums:
            if n - low > k:
                low = n
                result += 1

        return result
