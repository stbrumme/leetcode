class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)

        # replace each zero by a one
        sum1 += zeros1
        sum2 += zeros2

        # and fix one zero such that sum1 == sum2
        # (which means the smaller sum is modified to match the bigger sum)
        if sum1 < sum2:
            return -1 if zeros1 == 0 else sum2
        if sum1 > sum2:
            return -1 if zeros2 == 0 else sum1

        return sum1 # or sum2
