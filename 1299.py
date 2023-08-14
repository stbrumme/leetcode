class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = -1
        result = []
        arr.reverse()
        for i in range(len(arr)):
            result.append(high)
            high = max(high, arr[i])

        result.reverse()
        return result
