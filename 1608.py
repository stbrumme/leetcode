class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        prev = -inf
        while nums:
            x = len(nums)
            if prev < x <= nums[0]:
                return x
            prev = heappop(nums)

        return -1
