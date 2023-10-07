class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False

        pos = 1
        while arr[pos - 1] < arr[pos]:
            pos += 1
        while pos < len(arr) and arr[pos - 1] > arr[pos]:
            pos += 1

        return pos == len(arr)
