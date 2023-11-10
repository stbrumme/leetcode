class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        result = 0
        for a in arr1:
            pos = bisect_left(arr2, a)
            if pos < len(arr2) and abs(arr2[pos    ] - a) <= d:
                continue
            if pos > 0         and abs(arr2[pos - 1] - a) <= d:
                continue
            result += 1
        return result
