class Solution:
    def getpos(self, nums, value):
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2;
            if nums[mid] < value:
                low = mid + 1
            else:
                high = mid
        return low

    def countSmaller(self, nums: List[int]) -> List[int]:
        # modified sorting
        result = []
        done = []
        for i in reversed(nums):
            pos = self.getpos(done, i)
            done.insert(pos, i)
            result.append(pos)

        return reversed(result)
