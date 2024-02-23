class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                if nums[i] == nums[j]: # not needed but makes it a bit faster
                    continue

                for k in range(j + 1, size):
                    if nums[i] != nums[k] and nums[j] != nums[k]:
                        result += 1

        return result
