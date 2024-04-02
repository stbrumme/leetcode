class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        size = len(arr1) # == len(arr2)

        # minimize / maximize each absolute value each pair arr1/arr2
        diff1 = [  arr1[i] + arr2[i] + i for i in range(size) ]
        result =             max(diff1) - min(diff1)
        diff2 = [  arr1[i] - arr2[i] + i for i in range(size) ]
        result = max(result, max(diff2) - min(diff2))
        diff3 = [ -arr1[i] + arr2[i] + i for i in range(size) ]
        result = max(result, max(diff3) - min(diff3))
        diff4 = [ -arr1[i] - arr2[i] + i for i in range(size) ]
        return   max(result, max(diff4) - min(diff4))
