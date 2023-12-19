class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        low = inf
        result = []
        for i in range(1, len(arr)):
            a = arr[i - 1]
            b = arr[i]
            diff = b - a
            if   diff <  low:
                result = [ [ a, b ] ]
                low = diff
            elif diff == low:
                result.append([ a, b ])

        return sorted(result)
