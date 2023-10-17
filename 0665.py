class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [ -999999 ] + nums + [ +999999 ]
        misplaced = 0
        # 2 passes: fix element in first pass
        for i in range(2, len(nums)):
            if  nums[i] < nums[i - 1]:
                if nums[i] >= nums[i - 2]:
                    # a small number between two bigger
                    nums[i - 1] = nums[i]
                else:
                    # a bigger number
                    nums[i] = nums[i - 1]
                misplaced += 1
                if misplaced == 2:
                    return False

        # must be ordered in second pass
        for i in range(2, len(nums)):
            if  nums[i] < nums[i - 1]:
                return False
        return True
