class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # pad very small and very big numbers to simplify my algorithm
        arr   = [ -1 ] + arr + [ 10**10 ]
        size  = len(arr)

        left  = 0
        right = size - 1
        # find left and right part of the array that is properly sorted
        while left < right and arr[left]      <= arr[left + 1]:
            left  += 1
        while left < right and arr[right - 1] <= arr[right]:
            right -= 1

        # everything's sorted
        if left == right:
            return 0

        # worst case: remove all but one element
        result = size - 1

        # even though arr[0...left] and arr[right...size-1] are properly sorted,
        # there might be a mismatch between arr[left] and arr[right]
        for l in reversed(range(left + 1)):
            for r in range(right, size):
                length = r - l - 1
                if length >= result: # no improvement
                    break
                if arr[l] <= arr[r]: # yep, all sorted now
                    result = length

        return result
