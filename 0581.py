class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # O(nlogn), not O(n)
        n2 = sorted(nums.copy())

        left = right = None
        for i in range(len(nums)):
            if nums[i] != n2[i]:
                left  = i if left == None else left
                right = i

        return 0 if left == None else right - left + 1