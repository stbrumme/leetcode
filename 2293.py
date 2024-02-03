class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        size = len(nums)

        # basic cases
        if size == 1:
            return nums[0]
        if size == 2:
            return min(nums)

        # general case
        next = []
        for i in range(0, size, 4):
            next.append(min(nums[  i  ], nums[i + 1]))
            next.append(max(nums[i + 2], nums[i + 3]))

        # recursion
        return self.minMaxGame(next)
