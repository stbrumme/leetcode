class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()

        i = 1
        while nums[i-1] == i: # zero-indexed
            i += 1

        j = i
        while j <= len(nums) and nums[j-1] != j:
            j += 1

        if nums[i-1] < i:
            return [ i-1, j-1 ]
        else:
            return [ j, i ]
